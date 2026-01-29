# AI 选题生成系统 - 安装指南

## 快速安装

### 方法一：作为 Claude Code Plugin 安装（推荐）

1. **创建 Plugin 配置文件**

在项目根目录创建 `.claude-plugin/plugin.json`：

```json
{
  "name": "ai-topic-generator",
  "version": "1.0.0",
  "description": "AI选题生成系统 - 全自动从热点采集到选题审核",
  "author": "Your Name",
  "skills": [
    "./skills/hotspot-collector",
    "./skills/topic-generator",
    "./skills/topic-reviewer"
  ]
}
```

2. **安装到 Claude Code**

```bash
# 复制整个项目到 Claude Code plugins 目录
cp -r ai-topic-generator ~/.claude/plugins/

# 或者使用符号链接（便于开发）
ln -s /path/to/ai-topic-generator ~/.claude/plugins/ai-topic-generator
```

3. **启用 Plugin**

```bash
claude plugin enable ai-topic-generator
```

### 方法二：手动安装 Skills

1. **找到 Claude Code 的 skills 目录**

```bash
# macOS/Linux
~/.claude/skills/

# Windows
%USERPROFILE%\.claude\skills\
```

2. **复制各个 Skill**

```bash
cp -r skills/hotspot-collector ~/.claude/skills/
cp -r skills/topic-generator ~/.claude/skills/
cp -r skills/topic-reviewer ~/.claude/skills/
```

3. **复制 Agent 配置**

```bash
cp AGENTS.md ~/.claude/agents/ai-topic-generator.md
```

## 验证安装

启动 Claude Code 并测试：

```bash
claude

# 在对话中输入
列出所有可用的 skills

# 应该能看到：
# - hotspot-collector
# - topic-generator
# - topic-reviewer
```

## 首次使用

```
用户：开始今日选题生成
```

系统会自动创建 `output/` 目录并执行完整流程。

## 配置

### 1. 设置数据源权限

某些平台可能需要 API 密钥：

```bash
# 设置环境变量
export TWITTER_API_KEY="your_key"
export REDDIT_API_KEY="your_key"
```

### 2. 自定义输出目录

编辑 `AGENTS.md` 中的路径配置：

```markdown
"files": {
  "hotspots": "output/daily_hotspots/YYYY-MM-DD.json",
  "topics": "output/generated_topics/YYYY-MM-DD.json",
  "reviews": "output/review_reports/YYYY-MM-DD.json"
}
```

### 3. 调整审核标准

编辑 `skills/topic-reviewer/SKILL.md`：

```markdown
### 审核维度
- 选题价值 (权重: 30%)  # 可以调整权重
- 角度独特性 (权重: 25%)
...
```

## 故障排查

### 问题：Skills 无法加载

**检查**：
```bash
# 验证 SKILL.md 格式
cat skills/hotspot-collector/SKILL.md | head -5

# 应该看到 YAML frontmatter：
# ---
# name: hotspot-collector
# description: ...
# ---
```

**修复**：
- 确保每个 SKILL.md 都有正确的 frontmatter
- 检查文件权限（应该可读）

### 问题：找不到输出文件

**检查**：
```bash
# 确认输出目录存在
ls -la output/

# 应该有三个子目录：
# daily_hotspots/
# generated_topics/
# review_reports/
```

**修复**：
```bash
# 手动创建目录
mkdir -p output/{daily_hotspots,generated_topics,review_reports}
```

### 问题：Agent 调用失败

**检查**：
- 确认 AGENTS.md 在正确位置
- 验证 Skills 都已正确加载

**修复**：
- 重启 Claude Code
- 重新安装 Plugin/Skills

## 更新

### 更新 Skills

```bash
# 拉取最新代码
git pull origin main

# 重新复制到 Claude Code
cp -r skills/* ~/.claude/skills/

# 重启 Claude Code
```

### 更新 Agent 配置

```bash
cp AGENTS.md ~/.claude/agents/ai-topic-generator.md
```

## 卸载

### 卸载 Plugin

```bash
claude plugin uninstall ai-topic-generator
```

### 手动删除

```bash
# 删除 Skills
rm -rf ~/.claude/skills/hotspot-collector
rm -rf ~/.claude/skills/topic-generator
rm -rf ~/.claude/skills/topic-reviewer

# 删除 Agent 配置
rm ~/.claude/agents/ai-topic-generator.md
```

## 下一步

安装完成后，查看 [README.md](README.md) 了解详细使用方法。
