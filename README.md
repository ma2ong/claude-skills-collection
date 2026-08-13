# Claude Skills Collection - 专业写作与开发技能包

> 这是一个集成了多种专业能力的 Claude Skills 集合，涵盖内容创作、AI味审校、视觉设计、选题自动化等领域。

## 📦 包含的 Skills

| Skill | 触发关键词 | 核心功能 |
|-------|-----------|---------|
| **🚀 vibe-writer-pro** | 写文章、深度写作、专业写作 | 终极全流程写作助手，卡兹克方法论深度落地（HKR质检/四层自检L1-L4/AI角色边界），内置7维爆款质量门 |
| **✍️ khazix-writer** | 卡兹克风格、公众号长文 | 卡兹克公众号长文写作专版，4000-8000字，五种内容原型，活人感优先 |
| **🎯 ai-topic-generator** | 开始选题生成、采集热点 | 全自动选题系统：热点采集 → 选题生成 → 证据包研究 → 质量审核 |
| **hotspot-collector** | 采集热点、全网热点 | 多平台热点采集，互动量加权评分 + Top评论挖掘 |
| **aihot** | AI 日报、今天 AI 圈有什么 | 调 aihot.virxact.com 公开 API 拉中文 AI 资讯，无需 API Key |
| **topic-generator** | 选题、生成选题 | 基于热点生成高质量选题，支持评论层挖角 + COMPARISON对比选题模式 |
| **evidence-researcher** | 补证据、找来源、研究包 | 为选题补齐一手来源、数据、反方观点和风险提示 |
| **topic-reviewer** | 审核选题、选题质量 | 5维度审核 + 内容可做性诊断 + 证据包门槛 |
| **obsidian-exporter** | 导出选题、Obsidian | 将选题导出到 Obsidian 知识库 |
| **ai-proofreading** | 审校、AI味、人味、润色 | AI写作指纹诊断 + 必要改写 + 7维传播力评估 |
| **social-card-generator** | 封面、卡片、小红书图 | 生成微信21:9+1:1封面、小红书卡片组，并做尺寸/可读性检查 |
| **content-converter** | 转X、转微博、转小红书 | 长文转社交媒体内容 |
| **personal-knowledge-search** | 素材、案例 | 搜索个人素材库，提供真实案例 |

---

## 🧭 写作时该用哪个？

五个 skill 都跟"写"有关，但**触发时机不同**。按你手上有什么来选：

| 你手上有什么 | 你要什么 | 用这个 |
|---|---|---|
| 什么都没有，只有个方向 | 从选题一路做到草稿箱 | **vibe-writer-pro** |
| 已有 PDF / brief / 链接 / 素材 | 一篇 4000-8000 字成稿，卡兹克文风 | **khazix-writer** |
| 文章已经写完 | 降 AI 味、加人味 | **ai-proofreading** |
| 成稿 + 要发朋友圈/小红书/X | 长文改成各平台短内容 | **content-converter** |
| 成稿，缺封面 | 微信 21:9+1:1 封面、小红书卡片组 | **social-card-generator** |

一句话分界：**vibe-writer-pro 管"从零到发布"，khazix-writer 管"素材进、成稿出"。** 其余三个是接在成稿之后的独立工序，不要为了用它们而绕开主流程。

> v3.1.0 起 `vibe-writer` 已并入 `vibe-writer-pro`。它自称"vibe-writer-pro 的轻量版"，触发词却和后者高度重叠（两边都有"全流程写作"），实际效果是 Agent 随机二选一。它的四个参考文件已全部被 vibe-writer-pro 取代——配图部分尤其明显，vibe-writer-pro 有每 500-700 字一张的硬密度下限和 10 类配图决策表。

---

## 🎯 快速开始

### 安装方式

本仓库是一个 Claude Code **插件市场**，两条命令装完，重启 Claude Code 生效：

```bash
claude plugin marketplace add ma2ong/claude-skills-collection
claude plugin install topic-radar@claude-skills-collection    # 选题段（7 个 skill）
claude plugin install vibe-writing@claude-skills-collection   # 写作段（6 个 skill）
```

两个插件合起来就是完整流水线；只想要其中一段就只装一个。

| 插件 | 包含 | 装完能做什么 |
|---|---|---|
| `topic-radar` | ai-topic-generator / hotspot-collector / aihot / topic-generator / evidence-researcher / topic-reviewer / obsidian-exporter | 说一句「开始今日选题生成」，跑完热点采集 → 选题 → 证据包 → 审核 → 导出 |
| `vibe-writing` | vibe-writer-pro / khazix-writer / ai-proofreading / social-card-generator / content-converter / personal-knowledge-search | 从选题写到成稿，含 AI 味审校、封面卡片、多平台改写 |

验证装好了：

```bash
claude plugin details topic-radar     # 应列出 Skills (7)
claude plugin details vibe-writing    # 应列出 Skills (6)
```

<details>
<summary>不用插件，手动安装</summary>

Claude Code 只识别 `~/.claude/skills/<skill 名>/SKILL.md` 这一层，**直接 `git clone` 整个仓库到 `~/.claude/skills` 装不上任何 skill**（会得到一个没有根 `SKILL.md` 的空壳目录）。手动装必须把子目录逐个拷出来：

```bash
git clone https://github.com/ma2ong/claude-skills-collection.git /tmp/csc
for s in ai-topic-generator hotspot-collector aihot topic-generator \
         evidence-researcher topic-reviewer obsidian-exporter \
         vibe-writer-pro khazix-writer ai-proofreading \
         social-card-generator content-converter personal-knowledge-search; do
  cp -r "/tmp/csc/$s" ~/.claude/skills/
done
```

</details>

### 使用方法

直接在 Claude Code 中用自然语言描述需求：

```
# 自动化选题生成
"开始今日选题生成"

# 写作相关
"帮我审校这篇文章"
"启动 Vibe Writer，我想写一篇深度文章"

# 内容转换
"把这篇文章转成X的thread"
"生成一个文章配图"
```

---

## 📖 Skills 详解

### 🎯 ai-topic-generator - 全自动选题系统

**一句话开始**：
```
开始今日选题生成
```

系统会自动：
1. 📡 从多平台采集最新热点（Twitter、Reddit、GitHub、微博、知乎等）
2. 💡 分析并生成 TOP10 高质量选题（含事件描述、核心角度、标题建议）
3. 🔎 为选题补齐证据包（一手来源、反方观点、风险提示）
4. ✅ 智能审核选题质量，给出修改意见
5. 🔄 自动迭代优化，直到所有选题通过审核

**原本需要 2-3 小时的选题工作，现在只需 5-10 分钟！**

#### 完整流程

```
# 一键执行完整流程
开始今日选题生成，今天是2026年3月28日

# 分步执行
采集今日全网热点              # 使用 hotspot-collector
基于今日热点生成TOP10选题     # 使用 topic-generator
为今日选题补齐证据包           # 使用 evidence-researcher
审核今日生成的选题             # 使用 topic-reviewer
```

#### 输出示例：一次真实运行

下面是 **2026-02-06 真实跑出来的产物**，三个文件都在仓库里，可以点开看全文。看点是**一条热点能被追着走完全程**：`hs-001` → `topic-001` → 审核 91 分 PASS。

**1. 热点数据** — [`output/daily_hotspots/2026-02-06.json`](output/daily_hotspots/2026-02-06.json)（当天采集 4 条）

```json
{
  "id": "hs-001",
  "title": "Manus Acquisition by Meta",
  "platform": "Reddit/Hacker News",
  "heat_score": 98,
  "category": "AI/Business",
  "summary": "Meta reportedly acquired Manus for $2 billion, signaling a major move in the AI agent space.",
  "keywords": ["Meta", "Manus", "AI Agents", "Acquisition"],
  "relevance_score": 10
}
```

**2. 生成选题** — [`output/generated_topics/2026-02-06.json`](output/generated_topics/2026-02-06.json)（`source_hotspots` 回指 hs-001）

```json
{
  "topic_id": "topic-001",
  "rank": 1,
  "event_description": { "source_hotspots": ["hs-001"] },
  "core_angle": {
    "angle_title": "The AI Agent Wars: Why Meta Paid $2B for Manus",
    "unique_value": "Deep dive into how AI agents are the new OS."
  },
  "headline": {
    "primary": "Meta $20亿收购 Manus：AI Agent 时代的终局之战已经打响",
    "alternatives": ["为什么 Meta 愿意为 Manus 支付 20 亿美元？", "从社交巨头到 AI 代理：扎克伯格的下一次豪赌"]
  }
}
```

**3. 审核报告** — [`output/review_reports/2026-02-06.json`](output/review_reports/2026-02-06.json)（不是只给分，会指出该补什么）

```json
{
  "topic_id": "topic-001",
  "verdict": "PASS",
  "scores": { "topic_value": 95, "angle_uniqueness": 90, "headline_quality": 92, "feasibility": 85, "audience_match": 90 },
  "total_score": 91,
  "strengths": ["重大行业并购，话题性极强", "深度分析 AI Agent 对 Meta 战略的影响"],
  "improvements": ["可以增加对开源与闭源 Agent 竞争的对比"]
}
```

> 这份样本跑在 2026-02 的 schema 上。之后热点数据加了 `engagement` 和 `top_comments`（用高互动评论反推选题角度），选题加了 `topic_type`（含 `COMPARISON` 双热点对比模式），审核加了证据包门槛。字段定义以各 skill 的 `SKILL.md` 为准。

#### 效率对比

| 工作环节 | 传统方式 | 使用本系统 | 提升 |
|---------|---------|-----------|------|
| 热点采集 | 60-90分钟 | 2-3分钟 | **30x** |
| 选题筛选 | 30-60分钟 | 1-2分钟 | **30x** |
| 角度挖掘 | 20-30分钟 | 自动 | **∞** |
| 标题创作 | 10-20分钟 | 自动 | **∞** |
| 质量审核 | 10-15分钟 | 1分钟 | **10x** |
| **总计** | **2-3.5小时** | **5-10分钟** | **20-40x** |

---

### 🚀 vibe-writer-pro - 终极全流程写作助手

**功能**：融合多位大佬精华的完整写作系统，从选题到多平台分发的完整闭环。

**融合特性**：
- 🎯 **MapleShaw 的自动化流程**：完整工作流（需求理解 → 调研 → 选题 → 创作 → 审校 → 配图 → 分发）
- 🎨 **花叔的审校体系**：系统化降低 AI 味
- 🖼️ **Baoyu 的视觉美学**：HTML 信息图 + 真实截图混合配图
- ✨ **卡兹克写作方法论（深度落地）**：
  - HKR 选题质检（有趣/信息量/共鸣，及格两项）
  - 四层自检 L1-L4（禁词禁标点 → 节奏口语 → 内容质量 → 活人感）
  - 禁用标点规则（冒号/破折号→逗号，禁叙述类bullet point）
  - AI 角色边界（AI补证据，人来定观点）
- 📚 **个人素材库集成**：自动调用真实案例
- 🚀 **多平台分发**：一键生成 X/微博/小红书等平台内容
- 📊 **7维爆款质量门**：内置公众号爆款评估框架，低于5/7不得进入发布阶段

**完整工作流（7 个阶段）**：
1. **Phase 1: 需求理解与选题策划** - 深度调研 + 3 个差异化选题
2. **Phase 2: 初稿创作（Vibe 风格）** - 真实案例驱动 + 数据支撑
3. **Phase 3: 三遍审校 + 7维质量门** - 内容审校 → 风格审校 → 细节打磨 → 爆款评估
4. **Phase 3.5: 发布前质检关（有否决权）** - 七维门公式化升级 + 发布技术 Preflight，不达标不放行
5. **Phase 4: 视觉设计** - 封面图 + 章节配图 + 真实截图混合
6. **Phase 5: 多平台分发** - X Thread + 微博 + 小红书
7. **Phase 6: 最终交付** - 完整 Markdown + 配图 + 统计报告

> **🚦 Phase 3.5 是新增的发布前质检关**，专治"文章写得好但公众号 0 推送"。在七维门之上加四个公式化参考库 `vibe-writer-pro/references/`：`title_formulas.md`（标题打开率）、`hook_principles.md`（开头完读率）、`ai_fingerprints.md`（AI 指纹质量分）、`publish_preflight.md`（发布进草稿箱）。

**启动指令**：
```
"启动 Vibe Writer Pro，我想写一篇关于 [主题] 的文章"
```

---

### 📊 公众号爆款评估框架（7维）

所有写作和审校 Skill 均内置以下爆款质量标准：

| 维度 | 目标指标 | 核心公式 |
|------|---------|---------|
| **D1 标题与封面** | 打开率 ≥ 10% | 信息差 + 情绪触发 + 具体数字，命中 ≥ 2/3 |
| **D2 钩子结构** | 完读率 ≥ 30% | 前3行给出"这篇和你有关"信号，无铺垫废话 |
| **D3 内容密度节奏** | 收藏率 ≥ 3% | 段落2-4行，有可回收干货（清单/对比表/步骤） |
| **D4 情绪设计** | 分享率 ≥ 5% | 触发愤怒/焦虑/自豪/感动至少一种 |
| **D5 互动引导** | 评论率 ≥ 1% | 正文埋开放式问题，结尾显式互动引导 |
| **D6 关注转化** | 吸粉率 1-3% | 系列感 / 资源钩子 / 人设差异化 |
| **D7 传播裂变** | 二次传播 ≥ 60% | 至少1个可截图传播的信息单元（金句/数据图/对比表） |

> 核心链路：**标题拉打开 → 钩子拉完读 → 密度拉收藏 → 情绪拉转发 → 引导拉评论 → 人设拉关注 → 裂变拉二次传播**

---

### ✍️ khazix-writer - 卡兹克公众号长文写作

**来源**：[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)（1k+ stars）

**定位**："有见识的普通人在认真聊一件打动他的事。"

**核心特色**：
- 五大价值观底色（永远保持好奇 / 讲人话 / 真诚是唯一捷径）
- 五种内容原型（调查实验型 / 产品体验型 / 现象解读型 / 工具分享型 / 整活创意型）
- HKR 选题质检框架
- 四层自检（L1硬性规则 → L2节奏 → L3内容质量 → L4活人感）

**启动指令**：
```
"用卡兹克风格写一篇关于 [主题] 的公众号文章"
```

---

### 其他 Skills

#### 1. ai-proofreading - AI味审校
默认先做 AI 写作指纹诊断；用户明确要求后再进入必要改写。保留四遍审校（内容→风格→细节→传播力），输出7维爆款达标报告。

#### 2. hotspot-collector - 热点采集器

多平台热点采集，升级特性：
- **互动量加权评分**：`heat_score = 时效分×0.4 + 跨平台分×0.3 + 互动量分×0.3`
- **Top评论挖掘**：采集前3高互动评论，自动提炼 `implied_angle`（暗示选题角度）

#### 3. topic-generator - 选题生成器

基于热点生成高质量选题，升级特性：
- **评论层挖角**：读取 `top_comments.implied_angle`，以真实读者最关心的角度作为优先切入点
- **COMPARISON 模式**：检测到同赛道双热点时，自动生成"A vs B"对比选题（优先级排前3）

#### 4. evidence-researcher - 写作证据包研究员
为选题补齐一手来源、辅助来源、反方观点、缺失证据和风险提示，防止文章停留在热点复述。

#### 5. topic-reviewer - 选题审核官
5维度评估（价值度 + 独特性 + 落地性 + 传播潜力 + 证据充分度），并执行内容可做性诊断（文字洁癖、标题/封面、表达效率、认知落差、证据充分度）。

#### 6. social-card-generator - 社交卡片与封面生成器
生成微信公众号 `21:9 + 1:1` 封面组合、小红书 `1080 x 1440` 卡片组，并检查尺寸、溢出、短标题和缩略图可读性。

#### 7. aihot - AI 资讯查询
直接调用 [aihot.virxact.com](https://aihot.virxact.com) 的公开匿名 API 拉当日 AI 资讯，整理成中文简报。无需 API Key，`hotspot-collector` 会把它作为高优先信源调用。

#### 8. obsidian-exporter - Obsidian 导出器
将选题数据导出到 Obsidian 知识库，格式化为 Markdown。Vault 路径按 `OBSIDIAN_VAULT` 环境变量 → `config.json` 的 `vault_path` → 询问用户的顺序解析。

#### 9. content-converter - 分发助手
将长文浓缩并改写成社交媒体内容（X/微博/小红书/知乎）。

#### 10. personal-knowledge-search - 外脑
搜索个人素材库，获取真实案例和风格参考。

---

## 🏗️ 架构设计

### 渐进式披露 (Progressive Disclosure)

采用业界最佳实践的渐进式加载策略：

| 层级 | Token 消耗 | 加载时机 |
|------|-----------|---------|
| 元数据层 | ~100 tokens | 始终加载 |
| 指令层 | 3000-5000 tokens | 按需加载 |
| 资源层 | 按需 | 任务触发时 |

**Token 效率提升：75%+**

### 单一职责原则

每个 Skill 只做一件事：
- `writer` 不做 `coder` 的活
- `proofreader` 不做 `designer` 的活
- 通过 Skill 组合实现复杂工作流

### 脚本优于生成

确定性任务写成脚本，不占用 LLM Token：
- 图片上传脚本
- 文件处理脚本
- 格式转换脚本

---

## 📁 文件结构

> 下面是仓库的真实结构，与 `git ls-files` 一致。

```
claude-skills-collection/
├── .claude-plugin/marketplace.json   # 插件市场清单：topic-radar + vibe-writing
├── README.md
├── LICENSE                           # MIT
├── THIRD_PARTY_NOTICES.md            # 第三方来源与致谢
├── output/                           # 选题系统输出目录
│   ├── daily_hotspots/               # example.json + 2026-02-06 真实样本
│   ├── generated_topics/
│   └── review_reports/
│
│   ── 选题段（topic-radar）──────────────────────
├── ai-topic-generator/               # 总控：一句话跑完全流程
│   └── SKILL.md
├── hotspot-collector/                # 热点采集（互动量加权 + Top评论）
│   ├── SKILL.md  config.json
│   └── references/research-routing.md
├── aihot/                            # AI 资讯 API 查询
│   └── SKILL.md  config.json
├── topic-generator/                  # 选题生成（评论挖角 + COMPARISON）
│   ├── SKILL.md  config.json
│   └── memory/preferences.md
├── evidence-researcher/              # 证据包研究
│   └── SKILL.md
├── topic-reviewer/                   # 选题审核（5维度 + 证据门槛）
│   └── SKILL.md  config.json
├── obsidian-exporter/                # 导出到 Obsidian
│   └── SKILL.md  config.json
│
│   ── 写作段（vibe-writing）─────────────────────
├── vibe-writer-pro/                  # 主力写作助手
│   ├── SKILL.md  config.json  EXAMPLE.md
│   ├── references/                   # 8 个：ai_fingerprints / chinese-rhythm /
│   │                                 # hook_principles / publish_preflight /
│   │                                 # title_formulas / vibe_style_guide /
│   │                                 # viral-framework / workflow_rules
│   ├── scripts/check_prose.py        # 确定性文风检查
│   └── memory/preferences.md
├── khazix-writer/                    # 卡兹克风格长文（方法论来源见 THIRD_PARTY_NOTICES）
│   ├── SKILL.md  config.json
│   └── references/                   # content_methodology / style_examples
├── ai-proofreading/                  # AI 味审校
│   ├── SKILL.md  config.json
│   ├── references/                   # finalize-workflow / host-profile-workflow /
│   │                                 # scenario-presets
│   ├── scripts/anti_ai_gate.py       # 确定性 AI 味闸门（含单元测试）
│   └── memory/preferences.md
├── social-card-generator/            # 封面与卡片
│   └── SKILL.md
├── content-converter/                # 多平台改写分发
│   ├── SKILL.md  config.json
│   ├── references/xiaohongshu_tag_database.md
│   └── memory/preferences.md
└── personal-knowledge-search/        # 个人素材库检索
    ├── SKILL.md  config.json
    └── memory/preferences.md
```

**确定性资产**：`vibe-writer-pro/scripts/check_prose.py` 和 `ai-proofreading/scripts/anti_ai_gate.py`（带 `test_anti_ai_gate.py`）是靠代码而不是靠模型自觉执行的检查，这是本仓库和纯提示词写作 skill 的主要区别。

---

## 🔗 相关资源

- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Agent Skills 开放标准](https://agentskills.io)
- [Simon Willison: Skills vs MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)

---

## 📝 更新日志

### v3.2.0 (2026-08-13)

**vibe-writer-pro 渐进式披露改造 —— 单次调用成本降 75%**

- ⚡ **每次触发 16.8k → 4.2k token**（实测，`claude plugin details`）。此前 `SKILL.md` 1114 行、六个 Phase 的全部步骤内联，无论用户是要全流程还是只要审校，都得付全额
- 📚 六个 Phase 的正文逐字拆成 `references/phase-1..6-*.md` 分册，高级功能拆成 `advanced-features.md`。主文件只留骨架：Phase 表（含每关的过关条件）、四种快速启动模式、工作流检查清单、加载契约
- ✅ 逐行核对无内容丢失：原文 676 个非空行，新结构覆盖 676 个
- 🔗 **接上两个从来没被引用过的参考文件**：`vibe_style_guide.md`（8.9KB）和 `workflow_rules.md`（11.6KB）在旧版 `SKILL.md` 里出现 0 次，Agent 从未被指示加载过这 20KB 写作规则。这个缺口早于本次改造就存在
- ⚠️ 代价：跑完整流程时六个分册都要读，总量与从前相当。真正省下的是**只用其中一段**的场景（审校模式、配图模式），以及 skill 被触发但用户其实想做别的事时的误伤成本

### v3.1.0 (2026-08-13)

**写作 skill 去重 —— 消除路由歧义**

- 🔀 **`vibe-writer` 并入 `vibe-writer-pro`**：前者自称"vibe-writer-pro 的轻量版"，触发词却与后者高度重叠（两边都含"全流程写作"），Agent 实际是在两者间随机二选一。它的四个参考文件已被全面取代——尤其配图部分，`vibe-writer-pro` 有每 500-700 字一张的硬密度下限和 10 类配图决策表，而 `visual_guide.md` 还停在 Nano Banana / Unsplash 那一代
- 🧭 **新增「写作时该用哪个」路由表**，按"你手上有什么"分流五个写作相关 skill
- ✏️ `vibe-writer-pro` 与 `khazix-writer` 的 description 加入互斥路由说明：前者管"从零到发布"，后者管"素材进、成稿出"。`khazix-writer` 不再抢"公众号文章""长文写作"这类通用触发词
- 📦 `vibe-writing` 插件从 7 个 skill 变为 6 个。`ai-proofreading`（审校）和 `content-converter`（分发）**保持独立**——它们是接在成稿之后的不同工序，塞进写作 skill 只会让本已 16.9k token 的调用成本更高

### v3.0.0 (2026-08-13)

**分发方式变更 —— 从 clone 改为插件市场**

- 🔧 **修复安装即失效**：此前 README 让用户 `git clone` 到 `~/.claude/skills`，装出的目录没有根 `SKILL.md`，14 个 skill 一个都加载不了。新增 `.claude-plugin/marketplace.json`，拆成 `topic-radar`（选题段 7 个）+ `vibe-writing`（写作段 7 个），各一条命令装完
- 🔓 仓库转为 public，补 `LICENSE`（MIT）与 `THIRD_PARTY_NOTICES.md`（khazix-writer 方法论来源、aihot 的 Virxact API、可选外部工具）
- 🧹 清除私有内容：删掉硬编码本机路径的一次性脚本；`obsidian-exporter` 的 vault 路径改为 `OBSIDIAN_VAULT` 环境变量 → `config.json` → 询问；`publish_preflight.md` 里指向个人凭证位置和私有脚本的段落改写为通用描述
- 📄 README 打假：文件树曾列出两个不存在的输出目录和一个不存在的 assets 目录、漏掉 `aihot`、少报了参考文件与脚本、"其他 Skills" 有两个条目都编号 8 —— 全部按实际内容重写
- 🖼️ **输出示例换成真实产物**：README 里三份编造的 JSON 换成 2026-02-06 真实运行结果，全文入库可点开，一条热点贯穿全程（hs-001 → topic-001 → 91 分 PASS）
- 🎨 `social-card-generator` 新增「AI 生图后端」规格：`baoyu-imagine` 为默认后端、按资产类型划定使用边界（概念图走 AI、事实类走 HTML+Playwright、产品界面用真实截图）、调用前配置检查、缺后端时降级为纯排版并明确告知

### v2.2.0 (2026-04-08)

- ✨ **深度整合卡兹克写作方法论**，不再停留于"声称融合"
  - `vibe-writer-pro`：HKR 质检门槛、四层自检 L1-L4（含活人感）、禁用标点规则、AI 角色边界，新增 Rule 6/7
  - `vibe-writer`：同步升级四层自检体系、HKR 选题质检、活人感三要素
- 🆕 **NEW**: `khazix-writer` — 卡兹克公众号长文写作专版（来自 KKKKhazix/khazix-skills）
  - 五大价值观底色 + 五种内容原型 + HKR 框架 + 四层自检

### v2.1.0 (2026-03-28)

- 📊 **NEW**: 引入公众号爆款评估框架（7维），全面整合进写作与选题流水线
  - `vibe-writer-pro`：新增爆款质量门（D1-D7），低于5/7不得进入发布阶段
  - `ai-proofreading`：新增第四遍传播力审校，输出7维达标报告
  - `topic-reviewer`：新增传播潜力（15%权重）作为第4评分维度
  - `vibe-writer-pro/references/viral-framework.md`：完整7维框架参考文档
- 🔥 **NEW**: 借鉴 [last30days-skill](https://github.com/mvanhorn/last30days-skill) 升级热点与选题能力
  - `hotspot-collector`：互动量加权评分公式 + Top3评论挖掘（含 implied_angle）
  - `topic-generator`：评论层挖角（以高互动评论角度优先）+ COMPARISON 对比选题模式

### v2.0.0 (2026-01-29)

- 🎯 **NEW**: ai-topic-generator - 全自动选题系统
  - 集成 hotspot-collector（多平台热点采集）
  - 集成 topic-generator（智能选题生成）
  - 集成 topic-reviewer（5维度质量审核）
  - 集成 obsidian-exporter（知识库导出）
  - 完整工作流：采集 → 生成 → 审核 → 迭代 → 导出
  - 效率提升 20-40 倍
- 📊 新增 output 目录结构，标准化输出格式
- 📚 更新 README，添加详细使用指南

### v1.1.0 (2026-01-21)

- 🚀 **NEW**: vibe-writer-pro - 终极全流程写作助手
  - 融合 MapleShaw 自动化流程 + 花叔审校体系 + Baoyu 视觉美学 + 卡兹克 Vibe 文风
  - 6 阶段完整工作流：选题 → 创作 → 审校 → 配图 → 分发 → 交付
  - 真实案例驱动 + 系统化降低 AI 味
  - 多平台分发能力（X/微博/小红书）
- 📚 新增配套参考文档

### v1.0.0 (2026-01-21)

- ✨ 初始版本发布
- 📦 7 个专业 Skills
- 🎯 渐进式披露架构
- 💡 单一职责设计

---

## 📄 许可证

MIT License

---

*让 AI 写作更专业、更高效、更有人味。*
