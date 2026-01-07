import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_IN = ROOT / "README.md"
README_OUT = ROOT / "leetcode" / "README.md"

START = "<!---LeetCode Topics Start-->"
END = "<!---LeetCode Topics End-->"


def main() -> int:
    text = README_IN.read_text(encoding="utf-8", errors="replace")

    # Extract the block between markers (exclusive of markers)
    m = re.search(
        re.escape(START) + r"([\s\S]*?)" + re.escape(END),
        text,
        flags=re.MULTILINE,
    )
    if not m:
        content = (
            "# LeetCode\n\n"
            "_No LeetHub-generated topics found in the root README yet._\n"
        )
    else:
        extracted = m.group(1).strip()
        # Avoid duplicate H1s: LeetHub content often starts with "# LeetCode Topics"
        extracted = re.sub(r"^#\s+LeetCode Topics\s*", "## LeetCode Topics\n", extracted)
        content = "# LeetCode\n\n" + extracted + "\n"

    README_OUT.parent.mkdir(parents=True, exist_ok=True)
    README_OUT.write_text(content, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


