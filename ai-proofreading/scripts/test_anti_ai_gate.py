#!/usr/bin/env python3
from __future__ import annotations

import unittest

import anti_ai_gate


class AntiAiGateTest(unittest.TestCase):
    def test_model_residue_is_error(self) -> None:
        findings = anti_ai_gate.scan_text("结论如下。turn2search3")
        self.assertTrue(any(item.level == "error" and item.rule == "model-residue" for item in findings))

    def test_jargon_and_template_are_warnings(self) -> None:
        findings = anti_ai_gate.scan_text("让我们通过全链路能力赋能业务。")
        rules = {item.rule for item in findings if item.level == "warning"}
        self.assertEqual({"zh-jargon", "template-phrase"}, rules)

    def test_plain_chinese_quotes_are_not_flagged(self) -> None:
        self.assertEqual([], anti_ai_gate.scan_text("他说：“先核对数字，再下结论。”"))


if __name__ == "__main__":
    unittest.main()
