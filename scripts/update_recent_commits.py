"""
Update the "Recent commits" section in home.md with the latest commits by a GitHub user.

This script is designed to run in GitHub Actions and write a static markdown list
between:
  <!-- RECENT_COMMITS_START -->
  <!-- RECENT_COMMITS_END -->

It uses GitHub's commit search API (public commits). With the default GITHUB_TOKEN,
it will still only see public commits across GitHub.
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


START_MARKER = "<!-- RECENT_COMMITS_START -->"
END_MARKER = "<!-- RECENT_COMMITS_END -->"
CENTRAL_TZ_NAME = "America/Chicago"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", default="jdejones", help="GitHub username to query")
    parser.add_argument("--count", type=int, default=3, help="How many commits to render (1-10)")
    parser.add_argument("--file", default="home.md", help="Target markdown file to update")
    args = parser.parse_args()

    username = args.user.strip()
    count = max(1, min(10, int(args.count)))
    target = Path(args.file)

    token = os.environ.get("GITHUB_TOKEN", "").strip()

    items = fetch_recent_commits_by_author(username=username, count=count, token=token)
    new_block = render_markdown(items)

    original = target.read_text(encoding="utf-8")
    updated = replace_between_markers(original, new_block)

    if updated == original:
        print("No changes.")
        return 0

    target.write_text(updated, encoding="utf-8")
    print(f"Updated {target} with {len(items)} recent commits.")
    return 0


def fetch_recent_commits_by_author(*, username: str, count: int, token: str) -> list[dict]:
    # GitHub Search API: commits
    # https://docs.github.com/en/rest/search/search?apiVersion=2022-11-28#search-commits
    q = f"author:{username}"
    url = (
        "https://api.github.com/search/commits"
        f"?q={urllib.parse.quote(q)}"
        "&sort=committer-date"
        "&order=desc"
        f"&per_page={count}"
    )

    headers = {
        # Commit search historically required a preview Accept header; include it for compatibility.
        "Accept": "application/vnd.github.cloak-preview+json, application/vnd.github+json",
        "User-Agent": "jdejones-github-io-recent-commits-script",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    data = http_get_json(url, headers=headers)
    items = data.get("items", [])
    if not isinstance(items, list):
        return []
    return items


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
    lines.append(f"_Last updated (Central): {now_central.strftime('%Y-%m-%d %H:%M %Z')}_")
    lines.append("")

    if not items:
        lines.append("_No recent public commits found._")
        return "\n".join(lines).rstrip() + "\n"

    for item in items:
        repo = ""
        repo_obj = item.get("repository") or {}
        if isinstance(repo_obj, dict):
            repo = str(repo_obj.get("full_name") or "")

        commit = item.get("commit") or {}
        msg = ""
        date = ""
        if isinstance(commit, dict):
            msg = str(commit.get("message") or "").splitlines()[0].strip()
            committer = commit.get("committer") or {}
            author = commit.get("author") or {}
            if isinstance(committer, dict) and committer.get("date"):
                date = str(committer.get("date"))
            elif isinstance(author, dict) and author.get("date"):
                date = str(author.get("date"))

        url = str(item.get("html_url") or "")

        date_short = format_datetime(date)
        repo_part = f"**{repo}**" if repo else "**(unknown repo)**"
        title = msg or "(no message)"
        link = f"[{escape_md(title)}]({url})" if url else escape_md(title)
        suffix = f" — {date_short}" if date_short else ""

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
    # Keep exactly one newline after START and before END for clean diffs.
    prefix = text[:start_end]
    suffix = text[end_idx:]

    inner = "\n" + new_inner.rstrip() + "\n"
    return prefix + inner + suffix


def format_datetime(iso: str) -> str:
    if not iso:
        return ""
    try:
        # GitHub returns ISO8601 like 2026-01-07T12:34:56Z
        iso_norm = iso.replace("Z", "+00:00")
        d = dt.datetime.fromisoformat(iso_norm)
        d_central = to_central(d)
        return d_central.strftime("%Y-%m-%d %H:%M %Z")
    except Exception:
        return iso


def escape_md(s: str) -> str:
    # Minimal escaping for markdown link text
    return s.replace("[", "\\[").replace("]", "\\]")


def to_central(d: dt.datetime) -> dt.datetime:
    """
    Convert an aware datetime to US Central time (America/Chicago).
    Falls back to the original datetime if zoneinfo isn't available.
    """
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


