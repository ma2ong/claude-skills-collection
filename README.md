# Claude Skills Collection - 专业写作与开发技能包

> 这是一个集成了多种专业能力的 Claude Skills 集合，涵盖内容创作、AI味审校、视觉设计、选题自动化等领域。

## 📦 包含的 Skills

| Skill | 触发关键词 | 核心功能 |
|-------|-----------|---------|
| **🚀 vibe-writer-pro** | 写文章、深度写作、专业写作 | 终极全流程写作助手，融合 MapleShaw + 花叔 + Baoyu + 卡兹克，内置7维爆款质量门 |
| **🎯 ai-topic-generator** | 开始选题生成、采集热点 | 全自动选题系统：热点采集 → 选题生成 → 质量审核 |
| **hotspot-collector** | 采集热点、全网热点 | 多平台热点采集，互动量加权评分 + Top评论挖掘 |
| **topic-generator** | 选题、生成选题 | 基于热点生成高质量选题，支持评论层挖角 + COMPARISON对比选题模式 |
| **topic-reviewer** | 审核选题、选题质量 | 4维度审核（含传播潜力），自动迭代优化 |
| **obsidian-exporter** | 导出选题、Obsidian | 将选题导出到 Obsidian 知识库 |
| **vibe-writer** | 写作助手、Vibe Writing | 全流程自动化写作 |
| **ai-proofreading** | 审校、AI味、人味、润色 | 四遍审校流程，系统化降低AI检测率，内置7维传播力评估 |
| **content-converter** | 转X、转微博、转小红书 | 长文转社交媒体内容 |
| **personal-knowledge-search** | 素材、案例 | 搜索个人素材库，提供真实案例 |

---

## 🎯 快速开始

### 安装方式

```bash
# 克隆到 Claude Skills 目录
cd ~/.claude/skills
git clone https://github.com/ma2ong/claude-skills-collection.git
```

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
3. ✅ 智能审核选题质量，给出修改意见
4. 🔄 自动迭代优化，直到所有选题通过审核

**原本需要 2-3 小时的选题工作，现在只需 5-10 分钟！**

#### 完整流程

```
# 一键执行完整流程
开始今日选题生成，今天是2026年3月28日

# 分步执行
采集今日全网热点              # 使用 hotspot-collector
基于今日热点生成TOP10选题     # 使用 topic-generator
审核今日生成的选题             # 使用 topic-reviewer
```

#### 输出示例

执行完成后，系统会生成三个文件：

**1. 热点数据** `output/daily_hotspots/2026-03-28.json`
```json
{
  "id": "hs-001",
  "title": "Apple选择Gemini而非ChatGPT为新一代Siri提供动力",
  "platform": "Twitter/Ars Technica",
  "engagement": { "likes": 12400, "reposts": 3200, "comments": 890, "total": 16490 },
  "heat_score": 98,
  "top_comments": [
    { "text": "This is huge for Google's ad business...", "likes": 2100, "implied_angle": "Gemini接入苹果对谷歌广告收入的影响" }
  ],
  "category": "AI/科技巨头"
}
```

**2. 生成选题** `output/generated_topics/2026-03-28.json`
```json
{
  "topic_id": "topic-001",
  "topic_type": "COMPARISON",
  "rank": 1,
  "headline": { "primary": "Gemini vs ChatGPT：苹果押注背后，谁才是AI助手的真正赢家" },
  "core_angle": {
    "angle_title": "从高互动评论看：开发者最关心的不是功能，而是数据隐私",
    "angle_from_comments": "角度来源：高互动评论"
  }
}
```

**3. 审核报告** `output/review_reports/2026-03-28.json`
```json
{
  "summary": { "total_topics": 10, "passed": 8, "needs_revision": 2, "overall_quality": "优秀" }
}
```

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
- 🎯 **MapleShaw 的自动化流程**：10 步完整工作流
- 🎨 **花叔的审校体系**：三遍审校系统化降低 AI 味
- 🖼️ **Baoyu 的视觉美学**：高质量配图设计
- ✨ **卡兹克的 Vibe 文风**：像懂技术的老朋友聊天
- 📚 **个人素材库集成**：自动调用真实案例
- 🚀 **多平台分发**：一键生成 X/微博/小红书等平台内容
- 📊 **7维爆款质量门**：内置公众号爆款评估框架，低于5/7不得进入发布阶段

**完整工作流（6 个阶段）**：
1. **Phase 1: 需求理解与选题策划** - 深度调研 + 3 个差异化选题
2. **Phase 2: 初稿创作（Vibe 风格）** - 真实案例驱动 + 数据支撑
3. **Phase 3: 三遍审校 + 7维质量门** - 内容审校 → 风格审校 → 细节打磨 → 爆款评估
4. **Phase 4: 视觉设计** - 封面图 + 章节配图 + 真实截图混合
5. **Phase 5: 多平台分发** - X Thread + 微博 + 小红书
6. **Phase 6: 最终交付** - 完整 Markdown + 配图 + 统计报告

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

### 其他 Skills

#### 1. vibe-writer - 氛围感写作助手
全流程自动化写作，从调研到发布一站式服务。

#### 2. ai-proofreading - AI味审校
系统化降低 AI 检测率，**四遍审校**（内容→风格→细节→传播力），输出7维爆款达标报告。

#### 3. hotspot-collector - 热点采集器

多平台热点采集，升级特性：
- **互动量加权评分**：`heat_score = 时效分×0.4 + 跨平台分×0.3 + 互动量分×0.3`
- **Top评论挖掘**：采集前3高互动评论，自动提炼 `implied_angle`（暗示选题角度）

#### 4. topic-generator - 选题生成器

基于热点生成高质量选题，升级特性：
- **评论层挖角**：读取 `top_comments.implied_angle`，以真实读者最关心的角度作为优先切入点
- **COMPARISON 模式**：检测到同赛道双热点时，自动生成"A vs B"对比选题（优先级排前3）

#### 5. topic-reviewer - 选题审核官
**4维度**评估（价值度35% + 独特性25% + 落地性25% + **传播潜力15%**），自动迭代优化直到通过审核。

#### 6. obsidian-exporter - Obsidian 导出器
将选题数据导出到 Obsidian 知识库，格式化为 Markdown。

#### 7. content-converter - 分发助手
将长文浓缩并改写成社交媒体内容（X/微博/小红书/知乎）。

#### 8. personal-knowledge-search - 外脑
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

```
claude-skills-collection/
├── README.md                        # 本文件
├── output/                          # 选题系统输出目录
│   ├── daily_hotspots/              # 每日热点数据（含 engagement + top_comments）
│   ├── generated_topics/            # 生成的选题（含 topic_type + comparison_subjects）
│   └── review_reports/              # 审核报告
├── ai-topic-generator/              # AI选题生成系统（总控）
│   └── SKILL.md
├── hotspot-collector/               # 热点采集器（互动量加权 + Top评论）
│   └── SKILL.md
├── topic-generator/                 # 选题生成器（评论挖角 + COMPARISON模式）
│   ├── SKILL.md
│   └── memory/
│       └── preferences.md
├── topic-reviewer/                  # 选题审核官（4维度含传播潜力）
│   └── SKILL.md
├── obsidian-exporter/               # Obsidian导出器
│   └── SKILL.md
├── vibe-writer-pro/                 # 终极全流程写作助手
│   ├── SKILL.md
│   └── references/
│       ├── viral-framework.md       # 公众号爆款7维评估框架（核心参考）
│       ├── vibe_style_guide.md
│       └── workflow_rules.md
├── vibe-writer/                     # 总控写作助手
│   ├── SKILL.md
│   └── references/
├── ai-proofreading/                 # AI味审校（四遍审校 + 7维传播力）
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── content-converter/               # 内容转换
│   └── SKILL.md
└── personal-knowledge-search/       # 素材搜索
    └── SKILL.md
```

---

## 🔗 相关资源

- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Agent Skills 开放标准](https://agentskills.io)
- [Simon Willison: Skills vs MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)

---

## 📝 更新日志

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
