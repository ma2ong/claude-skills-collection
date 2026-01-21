# AI Proofreading Skill - 内容审校与AI味消除

> 这是一个专注于降低AI检测率、增加内容人味的专业写作技能包。

## 📦 包含内容

| 组件 | 说明 |
|------|------|
| **ai-proofreading** | 核心审校技能，三遍审校流程，系统化降低AI检测率 |

## 🎯 核心特性

### 1. 三遍审校流程

系统化执行三层审校，确保内容自然流畅：

- **第一遍**：内容审校（事实准确性、逻辑清晰性、原创性检查）
- **第二遍**：风格审校（去除6大类AI腔）
- **第三遍**：细节打磨（句子节奏、段落长度、标点使用）

### 2. AI腔识别与改写

精准识别并系统化改写以下AI腔特征：

- ✅ **套话连篇**：删除"在当今XX飞速发展的时代"等空洞开场
- ✅ **机械句式**：拆分"首先...其次...最后..."的僵硬结构
- ✅ **书面词汇**：将"显著"→"很明显"、"实现"→"做到"
- ✅ **结构机械**：打破段落长度对称，让节奏更自然
- ✅ **态度中立**：表达明确观点，避免各打五十大板
- ✅ **细节缺失**：加入真实时间、具体数字、具体案例

### 3. 渐进式披露架构

采用业界最佳实践的渐进式披露设计：

| 层级 | Token 消耗 | 加载时机 |
|------|-----------|---------|
| 元数据层 | ~100 tokens | 始终加载 |
| 指令层 | 3000-5000 tokens | 按需加载 |
| 资源层 | 按需 | 任务触发时 |

**Token 效率提升：75%+**

## 🚀 快速安装

### 方式 1：手动安装 (Claude Code)

```bash
# 复制文件夹到 Claude Skills 目录
cp -r ai-proofreading ~/.claude/skills/
```

### 方式 2：Git 克隆

```bash
cd ~/.claude/skills
git clone https://github.com/ma2ong/ai-proofreading.git
```

### 方式 3：子模块

```bash
git submodule add https://github.com/ma2ong/ai-proofreading.git .claude/skills/ai-proofreading
```

## 📖 使用方法

在 Claude Code 中直接说：

```
"帮我审校这篇文章"
"这篇太AI了，去掉AI味"
"降低这篇的AI检测率"
```

或指定使用：

```
使用 ai-proofreading 审校这段文字
```

## 📁 文件结构

```
ai-proofreading/
├── README.md              # 本文件
├── SKILL.md               # 核心Skill定义
├── references/            # 参考资料（按需加载）
├── scripts/               # 辅助脚本
└── assets/                # 静态资源
```

## 🔗 相关资源

- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Agent Skills 开放标准](https://agentskills.io)
- [Simon Willison: Skills vs MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)

## 📝 更新日志

### v1.0.0 (2026-01-21)

- ✨ 初始版本发布
- 📦 三遍审校流程
- 🎯 6大类AI腔识别
- 💡 渐进式披露架构

## 📄 许可证

MIT License

---

*让AI生成的内容读起来像真人写的。*
