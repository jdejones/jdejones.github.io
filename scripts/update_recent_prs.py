"""
Update the "Recent PRs" section in home.md with pull requests authored by a GitHub user.

This script is designed to run in GitHub Actions and write a static markdown list
between:
  <!-- RECENT_PRS_START -->
  <!-- RECENT_PRS_END -->

It uses GitHub's Search API (issues) with the `is:pr` qualifier (public PRs).
With the default GITHUB_TOKEN in Actions, it will still only see public PRs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


START_MARKER = "<!-- RECENT_PRS_START -->"
END_MARKER = "<!-- RECENT_PRS_END -->"
CENTRAL_TZ_NAME = "America/Chicago"
SEARCH_CAP = 1000  # GitHub search endpoints only return the first 1000 results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", default="jdejones", help="GitHub username to query")
    parser.add_argument(
        "--exclude-owner",
        default="",
        help="Exclude PRs where the repo owner matches this login (e.g. your own username).",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="How many PRs to render (0 = all available via search, max 1000).",
    )
    parser.add_argument("--file", default="home.md", help="Target markdown file to update")
    args = parser.parse_args()

    username = args.user.strip()
    exclude_owner = args.exclude_owner.strip()
    count = max(0, int(args.count))
    target = Path(args.file)

    token = os.environ.get("GITHUB_TOKEN", "").strip()

    items = fetch_pull_requests_by_author(
        username=username,
        token=token,
        exclude_owner=exclude_owner,
        limit=count,
    )
    new_block = render_markdown(items)

    original = target.read_text(encoding="utf-8")
    updated = replace_between_markers(original, new_block)

    if updated == original:
        print("No changes.")
        return 0

    target.write_text(updated, encoding="utf-8")
    print(f"Updated {target} with {len(items)} PRs.")
    return 0


def fetch_pull_requests_by_author(
    *,
    username: str,
    token: str,
    exclude_owner: str,
    limit: int,
) -> list[dict]:
    """
    Fetch PRs authored by `username`, optionally excluding repos owned by `exclude_owner`.

    Uses GitHub Search (issues) API. This API caps results to the first 1000 matches.
    """
    q = f"is:pr author:{username}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "jdejones-github-io-recent-prs-script",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    out: list[dict] = []
    per_page = 100
    page = 1

    while True:
        remaining = None
        if limit > 0:
            remaining = max(0, limit - len(out))
            if remaining == 0:
                break

        # Respect GitHub's 1000-result search cap.
        if (page - 1) * per_page >= SEARCH_CAP:
            break

        this_page = per_page
        if remaining is not None:
            this_page = min(this_page, remaining)

        url = (
            "https://api.github.com/search/issues"
            f"?q={urllib.parse.quote(q)}"
            "&sort=created"
            "&order=desc"
            f"&per_page={this_page}"
            f"&page={page}"
        )

        data = http_get_json(url, headers=headers)
        items = data.get("items", [])
        if not isinstance(items, list) or not items:
            break

        for item in items:
            if not isinstance(item, dict):
                continue
            repo_full = repo_full_name_from_api_url(str(item.get("repository_url") or ""))
            if exclude_owner and repo_full:
                owner = repo_full.split("/", 1)[0]
                if owner.lower() == exclude_owner.lower():
                    continue
            out.append(item)

        if len(items) < this_page:
            break

        page += 1

    return out


def http_get_json(url: str, *, headers: dict[str, str]) -> dict:
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        raise RuntimeError(f"GitHub API error ({e.code}): {body or e.reason}") from e
    except Exception as e:
        raise RuntimeError(f"Request failed: {e}") from e

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON from GitHub API: {e}") from e


def render_markdown(items: list[dict]) -> str:
    lines: list[str] = []
    now_central = to_central(dt.datetime.now(dt.timezone.utc))
    lines.append(f"_Last updated: {now_central.strftime('%Y-%m-%d %H:%M %Z')}_")
    lines.append("")

    if not items:
        lines.append("_No public PRs found._")
        return "\n".join(lines).rstrip() + "\n"

    for item in items:
        repo_full = repo_full_name_from_api_url(str(item.get("repository_url") or ""))
        repo_url = f"https://github.com/{repo_full}" if repo_full else ""

        title = str(item.get("title") or "").strip() or "(no title)"
        state = str(item.get("state") or "").strip()
        created_at = str(item.get("created_at") or "").strip()
        date_short = format_datetime(created_at)

        pr_url = str(item.get("html_url") or "").strip()
        pr_obj = item.get("pull_request") or {}
        if not pr_url and isinstance(pr_obj, dict):
            pr_url = str(pr_obj.get("html_url") or "").strip()

        repo_part = f"[**{escape_md(repo_full)}**]({repo_url})" if repo_url else "**(unknown repo)**"
        link = f"[{escape_md(title)}]({pr_url})" if pr_url else escape_md(title)

        suffix_bits: list[str] = []
        if date_short:
            suffix_bits.append(date_short)
        if state:
            suffix_bits.append(state)
        suffix = f" — {' · '.join(suffix_bits)}" if suffix_bits else ""

        lines.append(f"- {repo_part}: {link}{suffix}")

    return "\n".join(lines).rstrip() + "\n"


def replace_between_markers(text: str, new_inner: str) -> str:
    start_idx = text.find(START_MARKER)
    end_idx = text.find(END_MARKER)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise RuntimeError(
            f"Could not find markers in file. Expected {START_MARKER} ... {END_MARKER}"
        )

    start_end = start_idx + len(START_MARKER)
    prefix = text[:start_end]
    suffix = text[end_idx:]

    inner = "\n" + new_inner.rstrip() + "\n"
    return prefix + inner + suffix


def repo_full_name_from_api_url(url: str) -> str:
    # repository_url is like: https://api.github.com/repos/OWNER/REPO
    if not url:
        return ""
    try:
        parsed = urllib.parse.urlparse(url)
        path = (parsed.path or "").strip("/").split("/")
        if len(path) >= 3 and path[0] == "repos":
            owner = path[1]
            repo = path[2]
            if owner and repo:
                return f"{owner}/{repo}"
        return ""
    except Exception:
        return ""


def format_datetime(iso: str) -> str:
    if not iso:
        return ""
    try:
        iso_norm = iso.replace("Z", "+00:00")
        d = dt.datetime.fromisoformat(iso_norm)
        d_central = to_central(d)
        return d_central.strftime("%Y-%m-%d %H:%M %Z")
    except Exception:
        return iso


def escape_md(s: str) -> str:
    return s.replace("[", "\\[").replace("]", "\\]")


def to_central(d: dt.datetime) -> dt.datetime:
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    try:
        from zoneinfo import ZoneInfo  # py3.9+

        return d.astimezone(ZoneInfo(CENTRAL_TZ_NAME))
    except Exception:
        return d


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise

