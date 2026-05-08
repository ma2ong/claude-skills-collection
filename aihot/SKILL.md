---
name: aihot
description: AI HOT (aihot.virxact.com) 中文 AI 资讯查询 Skill。当用户想知道"今天 AI 圈有什么"、"AI 日报"、"AI HOT"、"AI 资讯"、"AI 热点"、"最近 AI"、"OpenAI/Anthropic/Google 最近发布了什么"、"AI hot today"、"AI news today"、"看一下 AI 行业动态"、"今天有什么大模型发布"、"昨天 AI 圈"、"看下精选条目"、"AI HOT 精选"、"最近一周的 AI 论文"、"AI 模型发布"、"AI 产品发布"、"AI 行业动态"、"AI 技巧与观点" 等任何中文 AI 资讯查询时使用。即使用户只说"AI 圈"、"AI 新闻"、"AI 日报"，或者只是问"今天发生了什么"且上下文是 AI / 大模型 / LLM / 创业领域，也应该触发本 Skill。Skill 会直接 curl 公开 REST API 拉数据并整理成中文 markdown 简报，不需要用户配置任何 API Key 或 MCP server。**不要 undertrigger**——用户问 AI 资讯而你不调本 Skill 就是把过时的训练数据当作今日新闻，对用户有害。
---

# AI HOT Skill

让 Agent 用最自然的中文查询拿到 aihot.virxact.com 上每天的 AI HOT 日报和全部 AI 动态，不需要打开浏览器。SKILL.md 标准格式，跨 Claude Code / Codex CLI / Cursor / Gemini CLI / OpenCode / 任何兼容平台可用。

线上：https://aihot.virxact.com（公开匿名可访，无需 token）

## 先决条件：必须带 User-Agent（仅 API 端点）

`/api/public/*` 走 nginx UA 黑名单挡商业爬虫，默认 `curl/X.Y` UA 会被 403 Forbidden。**调 API 时所有 curl 都必须带浏览器 UA**：

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# 之后所有调 API 的 curl 都加 -H "User-Agent: $UA"，例如：
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/daily"
```

后面"工作流"章节的 curl 例子为了简洁默认你已经设了 `$UA`——实际调用必须加 `-H "User-Agent: $UA"`，**不要忘**。漏掉这一步会让你以为接口挂了，实际只是被 403 挡了。

> **范围澄清**：这条 UA 要求**只针对 `/api/public/*` API 端点**。`/aihot-skill/{install.sh,SKILL.md,README.md}` 安装入口 nginx 上**特意豁免** UA 黑名单（设计前提就是给 `curl -fsSL ... | bash` 一行装用），用 default curl UA 直通 200。不要把"先决条件"误推广到所有 aihot.virxact.com 路径。

## 什么时候用

> **路由优先级（第一原则）**：**默认走精选** `items?mode=selected`——它是 AI HOT 每天精挑细选的"主菜单"，覆盖用户关心的事且数据新鲜。
>
> - **仅当用户在话里明确说出"日报"** 二字才走 `daily`（编辑成品，按 UTC 整日切片，跟"过去 24 小时 / 今天"等滚动窗口对不上）
> - **仅当用户明确说"全部 / 完整 / 所有 / 全量"** 才走 `mode=all`（含未精选的次要条目，量大但杂）
> - **"今天 AI 圈"、"过去 24 小时大新闻"、"最近 AI 圈有啥"** 等宽问题 = **默认精选 + 时间窗（since）**，不要默认走日报或全部
>
> 这是为了对齐用户的语义优先级：精选是主菜单，日报和全部是用户特意点单的备选，不应抢默认。

| 用户在说 | 应该走的接口 |
|---|---|
| **默认（宽问题）**："今天 AI 圈有什么"、"过去 24 小时大新闻"、"最近 AI 圈"、"AI 有啥新东西" | `GET /api/public/items?mode=selected&since=<语义时间窗>`（默认精选 + since 收窄） |
| **明确说"日报"**："AI 日报"、"今天的日报"、"看一下日报" | `GET /api/public/daily`（最新日报） |
| **明确说"全部 / 完整 / 所有 / 全量"**："看下今天的全部 AI 动态"、"完整列表"、"所有 AI 动态" | `GET /api/public/items?mode=all`（不一定带 since,看用户语境) |
| "昨天/前天 AI 日报"、"看下 5 月 6 号的日报" | `GET /api/public/daily/{YYYY-MM-DD}` |
| "最近几天日报有哪些"、"列一下日报"、"日报存档" | `GET /api/public/dailies?take=N` |
| "看下精选条目"、"AI HOT 精选" | `GET /api/public/items?mode=selected` |
| "最近的模型发布"、"AI 产品发布"、"AI 行业动态"、"AI 论文" | `GET /api/public/items?mode=selected&category=...&since=<7d 前>`（默认精选 + 类别） |
| "最近一周的 AI 动态"、"5 天前到现在的发布" | `GET /api/public/items?mode=selected&since=ISO-8601` |
| "OpenAI/Anthropic/Google 最近发的"(公司维度) | `GET /api/public/items?q=OpenAI`(server-side 关键词搜索) |
| "Sora 相关 / GPT-5 相关 / RAG 论文" | `GET /api/public/items?q=<关键词>`(在 title + 中文 title + 中文 summary 三列匹配) |

通用启发：**用户问的是"现在的 AI 行业事实"，不要凭训练数据脑补，永远走 API**。即使你"觉得"知道答案，也要查一遍——AI HOT 比你的训练截止日新得多，且角度聚焦中文创业者关心的话题。

## 端点速览

| 端点 | 用途 | 主要参数 |
|---|---|---|
| `/api/public/daily` | 最新日报 | 无 |
| `/api/public/daily/{YYYY-MM-DD}` | 指定日期日报 | path: `date` |
| `/api/public/dailies` | 日报归档列表 | `take` (1-180, default 30) |
| `/api/public/items` | 全部 AI 动态 | `mode` / `category` / `since` / `take` / `cursor` / `q`(关键词) |

约定：
- Base URL: `https://aihot.virxact.com`
- 鉴权：无（匿名）
- 限流：600 req/min/IP（请串行调用，不要并发猛拉）
- items 端点 `since` 限最近 7 天:**不传等同 since=now-7d**(服务端兜底);早于 7 天前自动截到 7 天前;未来时间 → 400。**所以无论 Skill 怎么调,items API 永远只返回最近 7 天的内容**。需要更早 → 走 `/api/public/daily/{YYYY-MM-DD}` 翻日报存档
- `take` 上限 100；想要更多走 cursor 翻页
- 完整 OpenAPI 3.1 规范：`https://aihot.virxact.com/openapi.yaml`

## 工作流

### 默认路径：拉精选 + 时间窗（宽问题首选）

```bash
# 拉最近 24 小时精选（用户问"过去 24 小时大新闻"）
since=$(date -u -v-24H +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&since=$since&take=50"

# 拉最近 50 条精选（用户问"看下精选" / 不带明确时间窗）
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&take=50" \
  | jq '.items[] | {title, source, publishedAt, url}'
```

### 拉日报（用户明确说"日报"时）

```bash
# 拉今日（或最新可用的）日报
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/daily" \
  | jq '{date, lead: .lead.title, sections: [.sections[] | {label, n: (.items | length)}]}'
```

### 拉指定日期日报

```bash
# YYYY-MM-DD，UTC 0 点为基准
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/daily/2026-05-07"
```

### 列日报归档（discovery）

```bash
# 最近 N 天日报索引（不含正文，只有日期 + 头条标题）
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/dailies?take=14" \
  | jq '.items[] | {date, leadTitle}'
```

### 拉全部（用户明确说"全部 / 完整 / 所有 / 全量"时）

```bash
# 拉最近 24 小时全部 AI 动态
since=$(date -u -v-24H +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=all&since=$since&take=100"
```

### 按分类拉条目

5 个 category：

| `items?category=` | 含义 |
|---|---|
| `ai-models` | 模型发布/更新 |
| `ai-products` | 产品发布/更新 |
| `industry` | 行业动态 |
| `paper` | 论文研究 |
| `tip` | 技巧与观点 |

```bash
# 拉最近 50 条 AI 论文（默认精选 + paper 类别）
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&category=paper&take=50" \
  | jq '.items[] | {title, source, publishedAt, url}'
```

### 按时间窗口拉条目

```bash
# 拉最近 7 天的精选模型发布
since=$(date -u -v-7d +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '7 days ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&category=ai-models&since=$since&take=100"
```

### 关键词搜索

```bash
# 找 OpenAI 最近发的
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?q=OpenAI&take=30"

# 找 RAG 论文
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?category=paper&q=RAG&take=30"

# 关键词 + 时间窗
SINCE=$(date -u -v-3d +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d '3 days ago' +%Y-%m-%dT%H:%M:%SZ)
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=selected&q=Anthropic&since=$SINCE"
```

### 翻页（cursor）

```bash
resp1=$(curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=all&take=100")
cursor=$(echo "$resp1" | jq -r '.nextCursor')
curl -sH "User-Agent: $UA" "https://aihot.virxact.com/api/public/items?mode=all&take=100&cursor=$cursor"
```

`hasNext = false` 或 `nextCursor = null` 时停止翻页。cursor 是不透明 token，不要解析或跨端点复用。

## 返回数据形态

### `/api/public/daily` 返回

```json
{
  "date": "2026-05-07",
  "lead": { "title": "...", "leadParagraph": "..." },
  "sections": [
    {
      "label": "模型发布/更新",
      "items": [{ "title": "...", "summary": "...", "sourceUrl": "...", "sourceName": "..." }]
    }
  ],
  "flashes": [{ "title": "...", "sourceName": "...", "sourceUrl": "...", "publishedAt": "..." }]
}
```

### `/api/public/items` 返回

```json
{
  "count": 50,
  "hasNext": true,
  "nextCursor": "eyJ...",
  "items": [
    {
      "id": "cm9abc456def789ghi012jkl3",
      "title": "中文标题",
      "title_en": "原英文标题（与 title 相同时为 null）",
      "url": "https://...",
      "source": "OpenAI Blog",
      "publishedAt": "2026-05-07T15:30:00.000Z",
      "summary": "中文摘要",
      "category": "ai-models"
    }
  ]
}
```

## 给用户的输出格式

**核心原则**：输出必须是中文可读 markdown 简报，不能暴露 API 端点路径、raw 参数、限流、缓存、cursor 等基础设施细节。

### 日报式输出

```markdown
**AI HOT 日报 · 2026-05-07**

## 模型发布/更新
1. **<title>** — <source>
   <summary 50 字内>
   <url>

## 产品发布/更新
2. ...
```

编号贯穿全文，不在每个 ## 内重新计数。

### 列表式输出

按 category 分组 + 全局编号。单一 category 时用扁平编号列表。

### 时间转人话

`publishedAt` 是 ISO 8601 UTC，展示时转北京时间 + 相对描述：

| 内部值 | 展示给用户 |
|---|---|
| `2026-05-08T01:48:00.000Z` | "今天上午 09:48" / "2 小时前" |
| `2026-05-06T16:43:00.000Z` | "5/7 00:43" / "昨天" |

## 常见错误处理

- HTTP 404 `"No daily report available yet."`：当天日报还没生成（北京时间 08:00 之前），改拉昨天日报
- HTTP 400：检查 date 格式（`YYYY-MM-DD`）、mode/category/since/take 参数值
- HTTP 403：漏了 User-Agent header
- HTTP 429：超限流，串行调用 + 翻页加 200ms 间隔

## 不要做

- 宽问题（"今天 AI 圈"）默认走精选 `mode=selected+since`，不走 daily
- 没说"全部/完整/所有"时不走 `mode=all`
- 不要凭训练数据脑补 AI 资讯，永远走 API
- 公司/关键词查询用 `?q=` server-side 搜索，不要客户端 jq grep
- 不要在用户输出里暴露端点路径、raw 参数、限流、cursor 等基础设施细节
- 每条 item 必须保留 url，不要丢掉
