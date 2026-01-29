# Claude Skills Collection - 专业写作与开发技能包

> 这是一个集成了多种专业能力的 Claude Skills 集合，涵盖内容创作、AI味审校、视觉设计、开发工作流等领域。

## 📦 包含的 Skills

| Skill | 触发关键词 | 核心功能 |
|-------|-----------|---------|
| **🚀 vibe-writer-pro** | 写文章、深度写作、专业写作 | **【NEW】** 终极全流程写作助手，融合 MapleShaw + 花叔 + Baoyu + 卡兹克 |
| **vibe-writer** | 写作助手、Vibe Writing、全流程写作 | 总控大脑，全流程自动化写作 |
| **ai-proofreading** | 审校、AI味、人味、润色 | 三遍审校流程，系统化降低AI检测率 |
| **baoyu-skills** | 配图、生成图片 | AI图片生成，基于Gemini和审美 |
| **topic-generator** | 选题、给几个方向 | 基于热点生成差异化选题 |
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
"帮我审校这篇文章"
"生成一个文章配图"
"给我几个选题方向"
"启动 Vibe Writer，我想写一篇深度文章"
```

---

## 📖 Skills 详解

### 🚀 NEW: vibe-writer-pro - 终极全流程写作助手

**功能**：融合多位大佬精华的完整写作系统，从选题到多平台分发的完整闭环。

**融合特性**：
- 🎯 **MapleShaw 的自动化流程**：10 步完整工作流（Brief → 调研 → 选题 → 初稿 → 审校 → 配图 → 分发）
- 🎨 **花叔的审校体系**：三遍审校系统化降低 AI 味（内容 → 风格 → 细节）
- 🖼️ **Baoyu 的视觉美学**：高质量配图设计，手绘风格封面 + 概念图
- ✨ **卡兹克的 Vibe 文风**：像懂技术的老朋友聊天，平和真诚有理有据
- 📚 **个人素材库集成**：自动调用真实案例，拒绝空洞说教
- 🚀 **多平台分发**：一键生成 X/微博/小红书等平台内容

**完整工作流（6 个阶段）**：
1. **Phase 1: 需求理解与选题策划** - 深度调研 + 3 个差异化选题
2. **Phase 2: 初稿创作（Vibe 风格）** - 真实案例驱动 + 数据支撑
3. **Phase 3: 三遍审校** - 内容审校 → 风格审校 → 细节打磨
4. **Phase 4: 视觉设计** - 封面图 + 章节配图 + 真实截图混合
5. **Phase 5: 多平台分发** - X Thread + 微博 + 小红书
6. **Phase 6: 最终交付** - 完整 Markdown + 配图 + 统计报告

**启动指令**：
```
"启动 Vibe Writer Pro，我想写一篇关于 [主题] 的文章"

# 快速模式（跳过选题）
"用 Vibe Writer Pro 写一篇关于 [主题] 的文章，标题是 [标题]，直接开始写"

# 审校模式（已有初稿）
"用 Vibe Writer Pro 审校这篇文章"
```

**与 vibe-writer 的区别**：
- vibe-writer-pro 是**完整的端到端系统**，包含选题、审校、配图、分发全流程
- vibe-writer 是**轻量级写作助手**，专注于初稿创作和基础审校
- 推荐优先使用 vibe-writer-pro 进行专业内容创作

---

### 1. vibe-writer - 氛围感写作助手

**功能**：全流程自动化写作，从调研到发布一站式服务。

**特点**：
- 像懂技术的老朋友聊天，平和真诚
- 强制要求真实案例和数据支撑
- 9 步闭环自动化流程
- 混合配图策略（概念图 + 真实截图）

**启动指令**：
```
"启动 Vibe Writer，我想写一篇关于 [主题] 的文章"
```

### 2. ai-proofreading - AI味审校

**功能**：系统化降低 AI 检测率，让内容读起来像真人写的。

**三遍审校流程**：
1. **内容审校**：事实准确性、逻辑清晰性、原创性
2. **风格审校**：去除 6 大类 AI 腔
3. **细节打磨**：句子节奏、段落长度、标点使用

**AI腔识别类型**：
- 套话连篇（"在当今XX飞速发展的时代"）
- 机械句式（"首先...其次...最后..."）
- 书面词汇（"显著"→"很明显"）
- 结构机械（段落长度对称）
- 态度中立（各打五十大板）
- 细节缺失（抽象描述多）

### 3. baoyu-skills - 视觉大师

**功能**：基于Gemini的高质量AI图片生成。

**核心能力**：
- 自动分析文章生成配图 (`baoyu-article-illustrator`)
- 自动生成3个版本的Prompt (通用/细节/风格化)
- 智能审美风格 (Notion风格/蓝图风格/水彩风格等)
- 自动调用 Gemini 生成图片

### 4. topic-generator - 策划顾问

**功能**：基于需求或热点生成高质量选题方向。

**特点**：
- 差异化角度挖掘
- 多维度评估选题价值
- 标题建议与优化

### 5. content-converter - 分发助手

**功能**：将长文浓缩并改写成社交媒体内容。

**支持平台**：
- X / Twitter
- 微博
- 小红书
- 知乎

**特点**：
- 保留核心观点
- 适配平台风格
- 钩子设计优化

### 6. personal-knowledge-search - 外脑

**功能**：搜索个人素材库，获取真实案例。

**特点**：
- 语义搜索能力
- 案例智能提取
- 风格参考匹配

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
├── README.md                    # 本文件
├── vibe-writer-pro/             # 【NEW】终极全流程写作助手
│   ├── SKILL.md
│   └── references/
│       ├── vibe_style_guide.md  # Vibe 风格指南
│       └── workflow_rules.md    # 工作流规则
├── vibe-writer/                 # 总控写作助手
│   ├── SKILL.md
│   └── references/              # 风格、视觉、工作流规则
├── ai-proofreading/             # AI味审校
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── baoyu-skills/                # 【外部集成】视觉配图
├── topic-generator/             # 选题生成
│   └── SKILL.md
├── content-converter/           # 内容转换
│   └── SKILL.md
├── personal-knowledge-search/   # 素材搜索
│   └── SKILL.md
```

---

## 🔗 相关资源

- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Agent Skills 开放标准](https://agentskills.io)
- [Simon Willison: Skills vs MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)

---

## 📝 更新日志

### v1.1.0 (2026-01-21)

- 🚀 **NEW**: vibe-writer-pro - 终极全流程写作助手
  - 融合 MapleShaw 自动化流程 + 花叔审校体系 + Baoyu 视觉美学 + 卡兹克 Vibe 文风
  - 6 阶段完整工作流：选题 → 创作 → 审校 → 配图 → 分发 → 交付
  - 真实案例驱动 + 系统化降低 AI 味
  - 多平台分发能力（X/微博/小红书）
- 📚 新增配套参考文档
  - Vibe 风格指南（vibe_style_guide.md）
  - 工作流规则（workflow_rules.md）

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
