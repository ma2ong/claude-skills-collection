---
name: vibe-writer-pro
description: |
  中文长文写作的默认全流程助手：选题质检 → 写作 → AI 味审校 → 配图 → 发布前质检，一路走到草稿箱。
  融合 MapleShaw 自动化流程、花叔审校体系、Baoyu 视觉美学、卡兹克写作方法论；
  内置 HKR 选题质检、五种内容原型、统一审校、AI 角色边界、配图密度硬下限。
  使用场景：写公众号文章、技术博客、深度长文、知识分享、产品文档。
  触发关键词：写文章、深度写作、全流程写作、专业写作、内容创作、帮我写一篇。
  路由：**手上没有成稿、需要从选题一路做到发布，就用本 skill**。
  如果用户点名要卡兹克文风、或者已经有完整素材只想要一篇成稿而不要全流程，改用 khazix-writer；
  文章已经写完只需要降 AI 味用 ai-proofreading；成稿要改成社媒短内容用 content-converter。
---

# Vibe Writer Pro - 终极写作助手 🚀

> **The Ultimate Content Creation System**
>
> 这不是一个简单的写作工具，而是你的**内容合伙人** + **创作教练** + **发布助手**。

## 核心理念 (Philosophy)

1. **真实第一 (Evidence First)**: 必须有真实案例、数据、代码片段支撑，拒绝空洞说教
2. **人味优先 (Human Touch)**: 系统化去除 AI 腔，像懂技术的老朋友在聊天
3. **流程自动化 (Auto Flow)**: 从需求理解到多平台发布的完整闭环
4. **视觉专业 (Visual Excellence)**: 高质量配图设计，概念图+真实截图混合策略

## 完整工作流 (Complete Workflow)

六个 Phase，每个 Phase 的详细步骤各有一个分册。**进入某个 Phase 前，必须先完整读完它的分册再动手** —— 主文件只有骨架和门槛，照骨架写等于跳过质检。

| Phase | 做什么 | 过关条件（不过不许进下一步） | 详细步骤 |
|---|---|---|---|
| 🎯 **1 需求与选题** | 理解需求 → 调研 → 出 3 个差异化选题 → 用户确认。含热点/深研/直写三种模式 | 材料门槛：≥1200 字需 ≥5 件素材，≥3000 字需 ≥8 件，每件有出处 | [`references/phase-1-brief-and-topic.md`](references/phase-1-brief-and-topic.md) |
| ✍️ **2 初稿创作** | 先定标题再写正文，按 Vibe 风格 + 中文韵律动笔 | **初稿阶段不要加载禁词表和 22 条指纹**（会写成缩手缩脚的东西）；核心判断必须有可核验证据 | [`references/phase-2-drafting.md`](references/phase-2-drafting.md) |
| 🔍 **3 统一审校** | 事实复核 → 推进检查 → 模型残留定点清理 → 脚本确定性检查 | `scripts/check_prose.py` 失败项清零；无纯解释段 | [`references/phase-3-review.md`](references/phase-3-review.md) |
| 🔍 **3.5 发布前质检关** | 标题公式、开头 6 检查点、AI 指纹、发布技术 Preflight | **有否决权**：任一不过就打回，不许进配图 | 同上，见分册末节 |
| 🎨 **4 视觉设计** | 封面 + 正文配图 + 按题材适配排版 | 正文图 ≥ 全文字数÷700 且 ≥ 3 种类型；浅底深字不可破 | [`references/phase-4-visual.md`](references/phase-4-visual.md) |
| 🚀 **5 多平台分发** | 询问分发需求 → 各平台改写 | 风格适配平台，不是同一份复制多处 | [`references/phase-5-distribution.md`](references/phase-5-distribution.md) |
| 📦 **6 最终交付** | 完整 Markdown + 图链接 + 统计 | 图床链接已嵌入，不留本地路径 | [`references/phase-6-delivery.md`](references/phase-6-delivery.md) |

高级功能（素材库集成、迭代优化模式、写作分析报告）见 [`references/advanced-features.md`](references/advanced-features.md)。


## 快速启动 (Quick Start)

### 完整模式

```
"启动 Vibe Writer Pro，我想写一篇关于 [主题] 的文章"
```

### 快速模式（跳过选题）

```
"用 Vibe Writer Pro 写一篇关于 [主题] 的文章，
标题是 [标题]，直接开始写"
```

### 审校模式（已有初稿）

```
"用 Vibe Writer Pro 审校这篇文章：[文章内容/文件路径]"
```

### 配图模式（已有文章）

```
"用 Vibe Writer Pro 为这篇文章配图：[文章内容/文件路径]"
```

---

## 注意事项 (Important Notes)

1. **真实性原则**：所有案例和数据必须来自材料或可靠来源；推断必须明确标注，不能冒充事实
2. **用户确认**：选题阶段必须等待用户确认，不自动开始创作
3. **风格一致性**：全文保持统一的 Vibe 风格，像真人在说话
4. **版权意识**：配图使用 AI 生成或用户提供，避免版权问题
5. **平台适配**：多平台分发时，深度理解每个平台的风格特点

---

## 工作流检查清单 (Workflow Checklist)

在每个阶段完成后，内部核对：

**Phase 1 - 需求与选题**
- [ ] 已理解用户需求
- [ ] 已完成深度调研
- [ ] 已提供 3 个差异化选题
- [ ] 已获得用户确认
- [ ] **材料门槛已过**（≥1200 字需 ≥5 件，≥3000 字需 ≥8 件，每件有出处）

**Phase 2 - 初稿创作**
- [ ] 已加载 Vibe 风格 + chinese-rhythm.md
- [ ] 初稿阶段未加载禁词表和 22 条指纹
- [ ] 开场平实有力，无套话
- [ ] 核心判断有可核验证据；未达到案例/数据目标时已缩小论点或标记缺口
- [ ] 技术内容只在帮助复现时提供真实代码

**Phase 3 - 统一审校**
- [ ] 事实准确性与冻结字段已复核
- [ ] **推进检查已跑**（无纯解释段，压缩试验已做）
- [ ] 模型残留、翻案句 7 变体和高风险模板已定点处理
- [ ] 句子、段落与格式符合场景和作者画像
- [ ] 具体细节全部有来路，未编造个人经历、案例或情绪
- [ ] `scripts/check_prose.py` 已跑，失败项清零，warning 已人工判断

**Phase 3.5 - 发布前质检关（有否决权）**
- [ ] 标题已套公式，张力≥2 项
- [ ] 开头 6 检查点通过
- [ ] AI 指纹无 🔴 强信号
- [ ] 发布技术 Preflight 7 项通过

**Phase 4 - 视觉设计**
- [ ] 封面图已生成
- [ ] 正文配图 ≥ 全文字数÷700 且 ≥ 3 种类型（不达标补图）
- [ ] 排版基调已按题材适配（非固定模板），浅底深字硬约束未破
- [ ] 所有图片已上传图床

**Phase 5 - 多平台分发**
- [ ] 已询问分发需求
- [ ] 各平台内容已生成
- [ ] 风格适配平台特点

**Phase 6 - 最终交付**
- [ ] 完整 Markdown 文件已输出
- [ ] 配图链接已嵌入
- [ ] 统计数据已提供

---

## 引用资源 (Resources)

本 Skill 会自动调用以下子 Skills：

- `topic-generator`: 选题生成
- `ai-proofreading`: 诊断、作者画像、定点修改与完整性复核
- `hotspot-collector`: Agent Reach 路由与热点采集
- `evidence-researcher`: 一手来源、反方观点与证据包
- `image-generator`: 配图生成与上传
- `content-converter`: 多平台分发
- `personal-knowledge-search`: 素材库搜索

确保这些 Skills 与 Agent Reach 已安装；渠道不可用时按 `source_coverage` 降级，不阻断写作。

**参考文件与加载时机**：

阶段分册（**进入该 Phase 前必读，不读就等于跳过质检**）：

| 文件 | 什么时候加载 |
|-----|------------|
| `references/phase-1-brief-and-topic.md` | 进入 Phase 1 |
| `references/phase-2-drafting.md` | 进入 Phase 2 |
| `references/phase-3-review.md` | 进入 Phase 3 与 3.5 |
| `references/phase-4-visual.md` | 进入 Phase 4 |
| `references/phase-5-distribution.md` | 进入 Phase 5 |
| `references/phase-6-delivery.md` | 进入 Phase 6 |
| `references/advanced-features.md` | 用户要素材库集成 / 迭代优化 / 写作分析报告时 |

专题参考（按需加载，不必整篇读）：

| 文件 | 什么时候加载 | 作用 |
|-----|------------|------|
| `references/vibe_style_guide.md` | **Phase 2 动笔时** | Vibe 风格核心原则、段落结构、AI 腔识别改写、写作模板 |
| `references/chinese-rhythm.md` | **Phase 2 动笔时** | 词序、照应、停顿、白话分寸 — 韵律 |
| `references/workflow_rules.md` | 需要各阶段输出格式规范、异常处理时 | 完整流程图、必守规则、各平台输出格式、异常处理 |
| `references/viral-framework.md` | Phase 3.5 | 公众号爆款 7 维评估框架 |
| `references/title_formulas.md` | Phase 3.5 | 75 标题公式（公众号适配版）— 打开率 |
| `references/hook_principles.md` | Phase 3.5 | 开头诊断 6 检查点 — 完读率 |
| `references/ai_fingerprints.md` | **Phase 3 审校时，不在初稿时** | 22 条 AI 指纹只诊断扫描 — 质量分 |
| `references/publish_preflight.md` | Phase 3.5 | 公众号发布 7 项硬检查 + errcode 排查 — 进草稿箱 |

**检查脚本**：

```bash
python scripts/check_prose.py 稿件.md
```

失败项（翻案句 / 黑话 / 模型路标）必须清零才能发布。警告项（长前置成分 / 重定语句 / 短段鼓点 / 开场重复 / 借喻混用）需要人工判断，脚本只发现形状，判断不了文章有没有人。

---

*Powered by the best of MapleShaw, Hua Shu, Baoyu, Kazike, and beyond.*

*让 AI 写作更专业、更高效、更有人味。* ✨


## 🧠 记忆与自进化 (Memory & Self-Evolution)

**1. 读取记忆**：
在开始任务前，**必须**读取 `memory/preferences.md`。这里保存了用户的个性化偏好、禁忌和习惯。请根据这些偏好调整你的工作方式。

**2. 接收反馈**：
任务完成后，如果用户提供了反馈（修改意见、批评或表扬）：
- **分析**：识别这是单次指令还是长期偏好。
- **记录**：如果是长期偏好，请立即使用 File Edit 工具将规则追加/更新到 `memory/preferences.md` 中。
- **确认**：告诉用户"已将此偏好记入我的长期记忆"。

**记忆文件位置**：`@path/memory/preferences.md`
