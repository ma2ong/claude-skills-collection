# 作者画像工作流

作者画像只记录能从真实样本重复观察到的风格信号。

## 样本要求

- 至少 3 篇，最好 5–10 篇。
- 使用同一发布场景的近半年样本。
- 优先作者本人未经 AI 润色的定稿。
- 样本不足时标记 `confidence: low`，不补全缺失维度。

## 提取维度

- 平均句长、短句（<15 字）和长句（>35 字）比例。
- 平均每段句数、单句成段频率、标题和列表密度。
- 常用动词、名词、第一人称和稳定口头表达。
- 开头方式、论证推进方式、收尾方式。
- 反问、倒装、括号、破折号、感叹号的真实频率。
- 明确不会使用的词、句式和格式。

同一特征至少在 3 个独立位置出现，才能写成稳定偏好。每项附 1–2 句样本证据；没有证据就留空。

## Profile 模板

```yaml
profile_name: author-scenario
scenario: wechat/blog/social/report
sample_files: []
sample_period: YYYY-MM to YYYY-MM
confidence: high/medium/low
rhythm:
  avg_chars_per_sentence:
  short_sentence_ratio:
  long_sentence_ratio:
  avg_sentences_per_paragraph:
structure:
  opening_patterns: []
  closing_patterns: []
  heading_policy:
voice:
  preferred_words: []
  recurring_moves: []
  punctuation_habits: []
forbidden:
  words: []
  sentence_shapes: []
  layouts: []
evidence: []
```

## 使用与更新

先应用事实边界和场景硬约束，再应用画像。每次收到“哪里不像”的反馈，只更新有证据的字段。内容主题不是风格；偶发用法不是稳定习惯；不要机械复读口头禅。
