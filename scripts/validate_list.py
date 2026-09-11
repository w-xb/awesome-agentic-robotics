#!/usr/bin/env python3
"""Repository-specific structural checks for Awesome Agentic Robotics."""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXTENDED = ROOT / "extended-reading.md"

NEW_ENTRY_RE = re.compile(r"^- \[(?P<date>\d{4}\.\d{1,2}) · (?P<title>.+?)\]\((?P<paper>https?://[^)]+)\) - (?P<description>.+)$")
OLD_ENTRY_RE = re.compile(r"^- \\?\[(?P<date>\d{4}\.\d{1,2})\] \*\*(?P<title>.+?)\*\* \[paper\]\((?P<paper>https?://[^)]+)\)(?P<tail>.*)$")
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|html)/(\d{4}\.\d+)")
LOCAL_LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")
TOC_LINK_RE = re.compile(r"^- \[[^]]+\]\(#([^)]+)\)$")

CANONICAL_SECTIONS = {
    "Surveys and Position Papers", "Agentic Robotics Architectures",
    "Agentic VLA and Embodied Foundation Models", "Self-Evolving Embodied Agents",
    "Embodied Memory", "Planning and Reasoning", "World Models and World-Action Models",
    "Verification, Recovery, and Safety Evaluation", "Verification and Safety Evaluation",
    "Failure Detection and Recovery", "Skill Learning and Tool Use", "Long-Horizon Manipulation",
    "Embodied Navigation", "Human-Robot Interaction", "Governance and Physical Safety",
    "Benchmarks and Datasets", "Open-Source Foundation Models", "Industrial Systems",
    "Foundations and Industrial Systems",
}
REQUIRED_FILES = {"LICENSE", "contributing.md", "extended-reading.md", ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/paper-suggestion.yml", ".github/workflows/repository-checks.yml"}

def github_slug(heading: str) -> str:
    heading = heading.strip().lower()
    chars = [c for c in heading if c.isalnum() or c in {" ", "-", "_"}]
    return "".join(chars).replace(" ", "-")

def fail(errors: list[str], message: str) -> None:
    errors.append(message)

def parse_entry(line: str):
    m = NEW_ENTRY_RE.match(line)
    if m:
        return m.group("date"), m.group("title"), m.group("paper")
    m = OLD_ENTRY_RE.match(line)
    if m:
        return m.group("date"), m.group("title"), m.group("paper")
    return None

def main() -> int:
    errors: list[str] = []
    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).exists():
            fail(errors, f"Missing required file: {relative}")
    readme = README.read_text(encoding="utf-8")
    extended = EXTENDED.read_text(encoding="utf-8")
    if "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)" not in readme:
        fail(errors, "README is missing the Awesome badge.")

    headings = {github_slug(line[3:]) for line in readme.splitlines() if line.startswith("## ")}
    in_contents = False
    for n, line in enumerate(readme.splitlines(), 1):
        if line == "## Contents":
            in_contents = True
            continue
        if in_contents and line.startswith("## "):
            in_contents = False
        if in_contents:
            m = TOC_LINK_RE.match(line)
            if m and m.group(1) not in headings:
                fail(errors, f"README:{n}: broken Contents anchor #{m.group(1)}")

    paper_urls=[]; arxiv_ids=[]; titles=[]; sections={}; current=None
    for n, line in enumerate(readme.splitlines(), 1):
        if line.startswith("## "):
            current=line[3:]
            continue
        if current not in CANONICAL_SECTIONS or not line.startswith("- "):
            continue
        parsed=parse_entry(line)
        if not parsed:
            fail(errors, f"README:{n}: unrecognized canonical entry format in '{current}'.")
            continue
        date,title,paper=parsed
        year,month=(int(x) for x in date.split("."))
        if not 1 <= month <= 12:
            fail(errors, f"README:{n}: invalid month {date}.")
        sections.setdefault(current,[]).append(((year,month),n,title))
        paper_urls.append(paper); titles.append(title)
        am=ARXIV_RE.search(paper)
        if am:
            arxiv_ids.append(am.group(1))

    if not paper_urls:
        fail(errors, "No canonical entries detected in README.md.")
    for section,entries in sections.items():
        dates=[d for d,_,_ in entries]
        if dates != sorted(dates, reverse=True):
            for prev,cur in zip(entries,entries[1:]):
                if prev[0] < cur[0]:
                    fail(errors, f"README:{cur[1]}: {section} is not newest-first near '{cur[2]}'.")
                    break
    for label,values in (("paper URL",paper_urls),("arXiv id",arxiv_ids),("title",titles)):
        dup=sorted(v for v,c in Counter(values).items() if c>1)
        if dup:
            fail(errors, f"Duplicate canonical {label}(s): {', '.join(dup)}")

    main_ids=set(arxiv_ids)
    ext_ids=set(ARXIV_RE.findall(extended))
    overlap=sorted(main_ids & ext_ids)
    if overlap:
        fail(errors, f"arXiv IDs appear in both canonical README sections and Extended Reading: {', '.join(overlap)}")

    for file_path in (README, EXTENDED, ROOT / "contributing.md"):
        text=file_path.read_text(encoding="utf-8")
        for m in LOCAL_LINK_RE.finditer(text):
            target=m.group(1).split("#",1)[0]
            if target and not (file_path.parent/target).exists():
                fail(errors, f"{file_path.name}: broken local link target: {m.group(1)}")
    if errors:
        print("Repository validation failed:\n")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"Repository validation passed: {len(paper_urls)} canonical entries across {len(sections)} sections.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
