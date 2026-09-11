#!/usr/bin/env python3
"""Lightweight structural checks for Awesome Agentic Robotics.

This intentionally checks repository-specific invariants that generic Markdown
linters do not know about: canonical entry format, date ordering, duplicates,
local links, and Contents anchors.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
EXTENDED = ROOT / "extended-reading.md"

ENTRY_RE = re.compile(
    r"^- \[(?P<date>\d{4}\.\d{1,2}) · (?P<title>.+?)\]\((?P<paper>https?://[^)]+)\) - (?P<description>.+)$"
)
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|html)/(\d{4}\.\d+)")
LOCAL_LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")
TOC_LINK_RE = re.compile(r"^- \[[^]]+\]\(#([^)]+)\)$")

CANONICAL_SECTIONS = {
    "Surveys and Position Papers",
    "Agentic Robotics Architectures",
    "Agentic VLA and Embodied Foundation Models",
    "Self-Evolving Embodied Agents",
    "Embodied Memory",
    "Planning and Reasoning",
    "World Models and World-Action Models",
    "Verification and Safety Evaluation",
    "Failure Detection and Recovery",
    "Skill Learning and Tool Use",
    "Long-Horizon Manipulation",
    "Embodied Navigation",
    "Human-Robot Interaction",
    "Governance and Physical Safety",
    "Benchmarks and Datasets",
    "Foundations and Industrial Systems",
}

REQUIRED_FILES = {
    "LICENSE",
    "contributing.md",
    "extended-reading.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/paper-suggestion.yml",
    ".github/workflows/awesome-lint.yml",
}


def github_slug(heading: str) -> str:
    heading = heading.strip().lower()
    chars: list[str] = []
    for char in heading:
        if char.isalnum() or char in {" ", "-", "_"}:
            chars.append(char)
    return "".join(chars).replace(" ", "-")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).exists():
            fail(errors, f"Missing required file: {relative}")

    readme = README.read_text(encoding="utf-8")
    extended = EXTENDED.read_text(encoding="utf-8")

    if "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)" not in readme:
        fail(errors, "README is missing the Awesome badge.")

    headings = {
        github_slug(line[3:])
        for line in readme.splitlines()
        if line.startswith("## ")
    }
    in_contents = False
    for line_number, line in enumerate(readme.splitlines(), start=1):
        if line == "## Contents":
            in_contents = True
            continue
        if in_contents and line.startswith("## "):
            in_contents = False
        if in_contents:
            match = TOC_LINK_RE.match(line)
            if match and match.group(1) not in headings:
                fail(errors, f"README:{line_number}: Contents target does not match a heading: #{match.group(1)}")

    paper_urls: list[str] = []
    arxiv_ids: list[str] = []
    titles: list[str] = []
    section_entries: dict[str, list[tuple[tuple[int, int], int, str]]] = {}
    current_section: str | None = None

    for line_number, line in enumerate(readme.splitlines(), start=1):
        if line.startswith("## "):
            current_section = line[3:]
            continue
        if current_section not in CANONICAL_SECTIONS or not line.startswith("- "):
            continue

        match = ENTRY_RE.match(line)
        if not match:
            fail(errors, f"README:{line_number}: canonical entry does not match the required format.")
            continue

        date = match.group("date")
        title = match.group("title")
        paper = match.group("paper")
        description = match.group("description")
        year, month = (int(part) for part in date.split("."))
        if not 1 <= month <= 12:
            fail(errors, f"README:{line_number}: invalid month in {date}.")

        if description[-1] not in ".!?…":
            fail(errors, f"README:{line_number}: description should end with punctuation.")

        urls = re.findall(r"\]\((https?://[^)]+)\)", line)
        duplicates = [url for url, count in Counter(urls).items() if count > 1]
        if duplicates:
            fail(errors, f"README:{line_number}: duplicate URL(s) in one entry: {', '.join(duplicates)}")

        section_entries.setdefault(current_section, []).append(((year, month), line_number, title))
        paper_urls.append(paper)
        titles.append(title)
        arxiv_match = ARXIV_RE.search(paper)
        if arxiv_match:
            arxiv_ids.append(arxiv_match.group(1))

    if not paper_urls:
        fail(errors, "No canonical entries were detected in README.md.")

    for section, entries in section_entries.items():
        dates = [date for date, _, _ in entries]
        if dates != sorted(dates, reverse=True):
            for previous, current in zip(entries, entries[1:]):
                if previous[0] < current[0]:
                    fail(
                        errors,
                        f"README:{current[1]}: {section} is not newest-first near '{current[2]}'.",
                    )
                    break

    for label, values in (("paper URL", paper_urls), ("arXiv id", arxiv_ids), ("title", titles)):
        duplicates = sorted(value for value, count in Counter(values).items() if count > 1)
        if duplicates:
            fail(errors, f"Duplicate canonical {label}(s): {', '.join(duplicates)}")

    main_ids = set(ARXIV_RE.findall(readme))
    extended_ids = set(ARXIV_RE.findall(extended))
    overlap = sorted(main_ids & extended_ids)
    if overlap:
        fail(errors, f"arXiv IDs appear in both README and Extended Reading: {', '.join(overlap)}")

    for file_path in (README, EXTENDED, ROOT / "contributing.md"):
        text = file_path.read_text(encoding="utf-8")
        for match in LOCAL_LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target:
                continue
            if not (file_path.parent / target).exists():
                fail(errors, f"{file_path.name}: broken local link target: {match.group(1)}")

    if errors:
        print("Repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Repository validation passed: {len(paper_urls)} canonical entries across {len(section_entries)} sections.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
