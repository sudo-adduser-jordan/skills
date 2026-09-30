#!/usr/bin/env python3
"""Screen vendored skill files for hidden text / steganographic tricks.

Fails (exit 1) when any finding is reported. Scans UTF-8 text files under
the given paths, skipping .git directories.

Checks:
  - zero-width / invisible chars: U+200B-U+200D, U+FEFF, U+2060, U+180E
  - bidirectional overrides: U+202A-U+202E, U+2066-U+2069, U+200E-U+200F
  - unicode tag block (U+E0000-U+E007F) often used to hide text
  - HTML/CSS hiding: display:none, visibility:hidden, font-size:0,
    color:transparent, color:#fff[fff], opacity:0, HTML comments in SKILL.md
  - long base64 blobs (>=200 chars) that may hide instructions
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

INVISIBLE = {
    "\u200b": "ZERO WIDTH SPACE",
    "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER",
    "\ufeff": "ZERO WIDTH NO-BREAK SPACE / BOM",
    "\u2060": "WORD JOINER",
    "\u180e": "MONGOLIAN VOWEL SEPARATOR",
}
BIDI = {
    "\u202a": "LEFT-TO-RIGHT EMBEDDING",
    "\u202b": "RIGHT-TO-LEFT EMBEDDING",
    "\u202c": "POP DIRECTIONAL FORMATTING",
    "\u202d": "LEFT-TO-RIGHT OVERRIDE",
    "\u202e": "RIGHT-TO-LEFT OVERRIDE",
    "\u2066": "LEFT-TO-RIGHT ISOLATE",
    "\u2067": "RIGHT-TO-LEFT ISOLATE",
    "\u2068": "FIRST STRONG ISOLATE",
    "\u2069": "POP DIRECTIONAL ISOLATE",
    "\u200e": "LEFT-TO-RIGHT MARK",
    "\u200f": "RIGHT-TO-LEFT MARK",
}
TAG_RE = re.compile(r"[\U000E0000-\U000E007F]")
BASE64_RE = re.compile(r"[A-Za-z0-9+/]{200,}={0,2}")
HIDE_CSS_RE = re.compile(
    r"display\s*:\s*none|visibility\s*:\s*hidden|font-size\s*:\s*0"
    r"|color\s*:\s*transparent|color\s*:\s*#fff(?:fff)?\b|opacity\s*:\s*0",
    re.IGNORECASE,
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

TEXT_EXTS = {
    ".md", ".json", ".yaml", ".yml", ".toml", ".txt",
    ".js", ".ts", ".py", ".sh", ".html", ".css",
}

findings: list[str] = []


def check_file(path: Path) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        findings.append(f"{path}: unreadable ({exc})")
        return
    for lineno, line in enumerate(text.splitlines(), 1):
        for ch, name in {**INVISIBLE, **BIDI}.items():
            if ch in line:
                findings.append(
                    f"{path}:{lineno}: hidden char {name} (U+{ord(ch):04X})"
                )
        if TAG_RE.search(line):
            findings.append(f"{path}:{lineno}: unicode tag-block char (hidden text)")
        if HIDE_CSS_RE.search(line):
            findings.append(f"{path}:{lineno}: CSS hiding pattern")
        for m in BASE64_RE.findall(line):
            findings.append(
                f"{path}:{lineno}: long base64 blob ({len(m)} chars, preview {m[:32]}...)"
            )
    if path.suffix == ".md" and HTML_COMMENT_RE.search(text):
        findings.append(f"{path}: contains HTML comment (review for hidden instructions)")


def iter_files(roots: list[str]) -> list[Path]:
    out: list[Path] = []
    for root in roots:
        base = Path(root)
        if base.is_file():
            out.append(base)
            continue
        if not base.exists():
            findings.append(f"{root}: path does not exist")
            continue
        for p in sorted(base.rglob("*")):
            if ".git" in p.parts:
                continue
            if p.is_file() and (p.suffix.lower() in TEXT_EXTS or p.name == "SKILL.md"):
                out.append(p)
    return out


def main(argv: list[str]) -> int:
    roots = argv[1:] or [".agents"]
    for path in iter_files(roots):
        check_file(path)
    if findings:
        print("hidden-text screen: FAILINGS FOUND", flush=True)
        for finding in findings:
            print(f"  - {finding}", flush=True)
        return 1
    print("hidden-text screen: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
