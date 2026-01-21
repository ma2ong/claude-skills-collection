# AI Writing Skill - 基于花叔审校架构的AI写作技能

> 这是一个基于花叔 Claude Skills 最佳实践创建的 AI 内容审校技能包。

## 📦 包含内容

| 组件 | 说明 |
|------|------|
| **ai-proofreading** | 核心审校技能，三遍审校流程，系统化降低AI检测率 |

## 🎯 核心特性

### 1. 三遍审校流程

- **第一遍**：内容审校（事实、逻辑、原创性）
- **第二遍**：风格审校（去除6大类AI腔）
- **第三遍**：细节打磨（句子、段落、标点）

### 2. AI腔识别与改写

系统化识别并改写以下AI腔：

- ✅ 套话连篇（"在当今XX飞速发展的时代"）
- ✅ 机械句式（"首先...其次...最后..."）
- ✅ 书面词汇（"显著"→"很明显"）
- ✅ 结构机械（段落长度相近）
- ✅ 态度中立（各打五十大板）
- ✅ 细节缺失（抽象描述多，具体例子少）

### 3. 花叔渐进式披露架构

基于花叔提出的渐进式披露原则：

- **元数据层** (100 tokens)：Skill基本信息和触发条件
- **指令层** (3000-5000 tokens)：详细执行流程和规则
- **资源层** (按需加载)：参考资料和示例

**Token 效率提升：75%**

## 🚀 快速安装

### 方式 1：手动安装 (Claude Code)

```bash
# 复制文件夹到 Claude Skills 目录
cp -r ai-proofreading ~/.claude/skills/
```

### 方式 2：Git 克隆

```bash
cd ~/.claude/skills
git clone https://github.com/ma2ong/AI-Writing-Skill.git
```

### 方式 3：子模块

```bash
git submodule add https://github.com/ma2ong/AI-Writing-Skill .claude/skills/ai-proofreading
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
AI-Writing-Skill/
├── README.md              # 本文件
├── SKILL.md               # 核心Skill定义
├── references/            # 参考资料（按需加载）
├── scripts/               # 辅助脚本
└── assets/                # 静态资源
```

## 🔗 相关资源

- [花叔的 Claude Skills 指南](https://mp.weixin.qq.com/s/x9UpqjuYzLb7I2ZZ932bNg)
- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Agent Skills 开放标准](https://agentskills.io)

## 📝 更新日志

### v1.0.0 (2026-01-21)

- ✨ 初始版本发布
- 📦 三遍审校流程
- 🎯 6大类AI腔识别
- 💡 渐进式披露架构

## 📄 许可证

MIT License

---

*Based on 花叔's Claude Skills architecture.*
