#!/usr/bin/env python3
"""Split a Markdown file into parts no larger than a size limit, at heading boundaries only.

- Splits happen only before a heading line, so a part never starts or ends inside a heading's
  text, a fenced code block (``` or ~~~, any length) or a table.
- Content is not lost or reordered: concatenating the parts' bodies gives the original sections.
- The original path becomes a table of contents: the text before the first section heading
  (title and intro) followed by a Markdown link to each part and the headings it contains.
- Files that already fit are written unchanged.
- As a tool it overwrites FILE with the contents page, and refuses to run on a file that is
  already split, so parts are never lost.

Usage as a tool:
  python3 tools/agentic-prompts/mdsplit.py FILE [--max-kib 400]
The default limit comes from max_file_kib in config.toml next to this script.
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t#]*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")

LABELS = {
    "en": {"toc": "Contents", "note": "This document is split into {n} files of at most {kib} KiB each, at heading boundaries.",
           "part": "Part {i}", "index": "Contents", "prev": "Previous", "next": "Next",
           "header": "Part {i} of {n} · {title}"},
    "ja": {"toc": "目次", "note": "この文書は、見出しの区切りで {n} ファイル（各 {kib} KiB 以下）に分割しています。",
           "part": "パート {i}", "index": "目次", "prev": "前へ", "next": "次へ",
           "header": "{title}（パート {i} / {n}）"},
}


def nbytes(text: str) -> int:
    return len(text.encode("utf-8"))


@dataclass
class Node:
    level: int            # 0 for the document root
    title: str
    lines: list[str] = field(default_factory=list)   # heading line + body before the first child
    children: list["Node"] = field(default_factory=list)

    def text(self) -> str:
        return "".join(self.lines) + "".join(c.text() for c in self.children)


@dataclass
class Unit:
    text: str
    headings: list[tuple[int, str]]  # headings that start inside this unit (level, title)


def parse(text: str) -> Node:
    """Build a heading tree. Lines inside fenced code blocks are never treated as headings."""
    root = Node(0, "")
    stack = [root]
    fence: tuple[str, int] | None = None
    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        m = FENCE.match(stripped)
        if fence is None and m:
            fence = (m.group(1)[0], len(m.group(1)))
        elif fence is not None and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1] and not m.group(2).strip():
            fence = None
        elif fence is None:
            h = HEADING.match(stripped)
            if h:
                node = Node(len(h.group(1)), h.group(2).strip(), [line])
                while stack[-1].level >= node.level:
                    stack.pop()
                stack[-1].children.append(node)
                stack.append(node)
                continue
        stack[-1].lines.append(line)
    if fence is not None:
        print("warning: unclosed code fence; the rest of the file is treated as code", file=sys.stderr)
    return root


def headings_of(node: Node, max_level: int) -> list[tuple[int, str]]:
    out = [(node.level, node.title)] if 0 < node.level <= max_level else []
    for c in node.children:
        out += headings_of(c, max_level)
    return out


def units_of(node: Node, budget: int, max_level: int) -> list[Unit]:
    """Whole node if it fits; otherwise its own lines, then each child's units (recursively)."""
    whole = node.text()
    if nbytes(whole) <= budget or not node.children:
        if nbytes(whole) > budget:
            print(f"warning: section '{node.title}' is {nbytes(whole) // 1024} KiB and has no subheadings; "
                  f"it is kept whole and exceeds the limit", file=sys.stderr)
        return [Unit(whole, headings_of(node, max_level))]
    out = [Unit("".join(node.lines), [(node.level, node.title)] if node.level <= max_level else [])]
    for c in node.children:
        out += units_of(c, budget, max_level)
    return out


def part_name(path: Path, i: int) -> str:
    name = path.name
    for suffix in (".ja.md", ".md"):
        if name.endswith(suffix):
            return f"{name[: -len(suffix)]}.part-{i:02d}{suffix}"
    return f"{name}.part-{i:02d}"


def stale_parts(path: Path) -> list[Path]:
    name = path.name
    for suffix in (".ja.md", ".md"):
        if name.endswith(suffix):
            stem = name[: -len(suffix)]
            return [p for p in path.parent.glob(f"{stem}.part-*{suffix}")
                    if re.fullmatch(re.escape(stem) + r"\.part-\d+" + re.escape(suffix), p.name)]
    return []


def split_text(text: str, path: Path, max_kib: float, lang: str = "en") -> dict[Path, str]:
    """Return {file path: content}. One entry if the text fits, else the contents file plus parts."""
    limit = int(max_kib * 1024)
    if nbytes(text) <= limit:
        return {path: text}
    L = LABELS.get(lang, LABELS["en"])
    root = parse(text)

    # Front matter for the contents file: text before the first heading, plus the single top heading
    # (the title) and its intro when the document has exactly one top-level heading.
    front = "".join(root.lines)
    sections = root.children
    title = path.stem
    if len(sections) == 1 and sections[0].children:
        top = sections[0]
        title = top.title
        front += "".join(top.lines)
        sections = top.children
    elif sections:
        title = sections[0].title

    reserve = 1024  # room for each part's navigation header and footer
    units: list[Unit] = []
    for s in sections:
        units += units_of(s, limit - reserve, max_level=4)

    groups: list[list[Unit]] = []
    for u in units:
        if groups and nbytes("".join(x.text for x in groups[-1]) + u.text) <= limit - reserve:
            groups[-1].append(u)
        else:
            groups.append([u])

    n = len(groups)
    names = [part_name(path, i) for i in range(1, n + 1)]
    files: dict[Path, str] = {}
    toc = [front.rstrip("\n"), "", f"## {L['toc']}", "", L["note"].format(n=n, kib=f"{max_kib:g}"), ""]
    for i, (g, name) in enumerate(zip(groups, names), start=1):
        heads = [h for u in g for h in u.headings]
        top_level = min((lvl for lvl, _ in heads), default=2)
        first = heads[0][1] if heads else ""
        last = heads[-1][1] if len(heads) > 1 else ""
        span = f"{first} … {last}" if last else first
        toc.append(f"- [{L['part'].format(i=i)}: {span}](./{name})")
        for lvl, t in heads:
            toc.append(f"{'  ' * (lvl - top_level + 1)}- {t}")

        nav = [f"[{L['index']}](./{path.name})"]
        if i > 1:
            nav.append(f"[{L['prev']}](./{names[i - 2]})")
        if i < n:
            nav.append(f"[{L['next']}](./{names[i]})")
        header = f"> {L['header'].format(i=i, n=n, title=title)}  \n> {' · '.join(nav)}\n\n"
        body = "".join(u.text for u in g)
        footer = f"\n---\n\n{' · '.join(nav)}\n"
        files[path.parent / name] = header + body.rstrip("\n") + "\n" + footer
    files[path] = "\n".join(toc).rstrip("\n") + "\n"
    return files


def is_split_index(text: str, path: Path) -> bool:
    """True if the text is a contents page produced by an earlier split of this path."""
    return any(f"](./{part_name(path, 1)})" in line for line in text.splitlines())


def write_split(text: str, path: Path, max_kib: float, lang: str = "en", clean: bool = False) -> list[Path]:
    """Write the file (split if needed) and return the written paths.

    clean=True removes part files left over from an earlier run. Use it only when `text` is the
    full source (as the generator does), never when `text` might itself be a contents page.
    """
    files = split_text(text, path, max_kib, lang)
    if clean:
        for old in stale_parts(path):
            if old not in files:
                old.unlink()
    for p, content in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
        size = nbytes(content)
        if size > max_kib * 1024:
            print(f"warning: {p.name} is {size / 1024:.1f} KiB, over the {max_kib:g} KiB limit", file=sys.stderr)
    return list(files)


def default_limit() -> float:
    cfg = Path(__file__).resolve().parent / "config.toml"
    if cfg.exists():
        return float(tomllib.loads(cfg.read_text(encoding="utf-8")).get("max_file_kib", 400))
    return 400.0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", type=Path)
    ap.add_argument("--max-kib", type=float, default=None, help="size limit per file in KiB (default: max_file_kib in config.toml, else 400)")
    ap.add_argument("--lang", choices=["en", "ja"], help="language of the contents labels (default: ja for .ja.md, else en)")
    args = ap.parse_args()
    limit = args.max_kib or default_limit()
    lang = args.lang or ("ja" if args.file.name.endswith(".ja.md") else "en")
    text = args.file.read_text(encoding="utf-8")
    if is_split_index(text, args.file):
        sys.exit(f"error: {args.file} is already a contents page of a split document; "
                 f"regenerate or restore the full file before splitting again")
    if stale_parts(args.file):
        sys.exit(f"error: part files for {args.file} already exist; remove them first")
    written = write_split(text, args.file, limit, lang)
    if len(written) == 1:
        print(f"{args.file}: {nbytes(text) / 1024:.1f} KiB, within {limit:g} KiB; not split")
    else:
        for p in written:
            print(f"wrote {p} ({p.stat().st_size / 1024:.1f} KiB)")


if __name__ == "__main__":
    main()
