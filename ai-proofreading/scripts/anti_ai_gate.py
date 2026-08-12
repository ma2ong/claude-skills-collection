#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    level: str
    rule: str
    line: int
    excerpt: str


RULES = [
    (
        "error",
        "model-residue",
        re.compile(
            r"contentReference|oaicite|turn\d+(?:search|news|view)\d*|"
            r"\[cite[:_]|grok_card|ppl-ai-file-upload"
        ),
    ),
    (
        "error",
        "assistant-framing",
        re.compile(r"^(?:Here is the revised version|以下是(?:修改|改写|润色)后的(?:版本|内容))", re.I),
    ),
    (
        "warning",
        "zh-jargon",
        re.compile(
            r"赋能|打通|闭环|抓手|对齐|链路|底层逻辑|一站式|全链路|端到端|"
            r"打造|致力于|助力|释放潜能|丝滑|无缝|干货满满"
        ),
    ),
    (
        "warning",
        "template-phrase",
        re.compile(
            r"让我们|值得注意的是|综上所述|总而言之|归根结底|说到底|"
            r"在这个.{0,30}的时代|记住[，,]真正"
        ),
    ),
    ("warning", "typographic-tell", re.compile(r"—|…|→|•")),
]


def scan_text(text: str) -> list[Finding]:
    findings: list[Finding] = []
    seen: set[tuple[str, int, str]] = set()
    for line_no, line in enumerate(text.splitlines(), 1):
        for level, rule, pattern in RULES:
            match = pattern.search(line)
            if not match:
                continue
            key = (rule, line_no, match.group(0))
            if key in seen:
                continue
            seen.add(key)
            findings.append(Finding(level, rule, line_no, line.strip()[:160]))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan a draft for deterministic AI-writing residue.")
    parser.add_argument("article", type=Path)
    parser.add_argument("--strict", action="store_true", help="Return non-zero for warnings too.")
    parser.add_argument("--json", action="store_true", help="Emit JSON findings.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    findings = scan_text(args.article.read_text(encoding="utf-8").lstrip("\ufeff"))
    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    elif findings:
        for item in findings:
            print(f"{item.level.upper()} {item.rule} line {item.line}: {item.excerpt}")
    else:
        print("No deterministic AI-writing residue found.")

    has_error = any(item.level == "error" for item in findings)
    return 1 if has_error or (args.strict and findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
