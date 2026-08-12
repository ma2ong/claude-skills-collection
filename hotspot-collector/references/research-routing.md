# Agent Reach 搜索路由

Agent Reach 只负责安装、体检和选择上游后端；实际读取仍调用当前激活的 CLI、MCP 或网页工具。

## 预检

```bash
agent-reach doctor --json
```

如果旧版不支持 `--json`，运行 `agent-reach doctor` 并按文本状态降级。命令不存在时继续使用当前环境已有的 OpenCLI、Web 搜索或浏览器，不让单个渠道阻断采集。

## 选择规则

1. 多后端或需要登录态的平台先读取 `active_backend`。
2. 使用本机安装的 `agent-reach` Skill 中对应平台的当前命令，不复制过时命令。
3. `status=ok` 才计入已覆盖渠道；`warn/off/error` 记录原因并走 fallback。
4. 不自动读取浏览器 Cookie，不把 Cookie、Token 或代理信息写进日志和输出。
5. Twitter、Reddit、小红书等社交内容只提供观点、热度和线索；重要事实回到一手来源核验。

## 信源分层

| 类型 | 用途 | 默认可靠性 |
|---|---|---|
| official / paper / repo | 事实、版本、参数、原始声明 | high |
| media | 事件补充、采访、行业背景 | medium |
| social | 观点、争议、使用场景、反方 | low |
| aggregator | 发现线索和跨平台热度 | low |

## 降级顺序

- 全网搜索不可用：官方网页 / GitHub / RSS / Jina Reader。
- Twitter 不可用：官方博客、follow-builders feed、RSS。
- Reddit 不可用：Hacker News、V2EX、公开网页讨论。
- 小红书不可用：微博、知乎、B站或公开网页案例。
- 任何渠道失败：保留其他渠道结果，并把缺口写入 `source_coverage.failed_channels`。

## 覆盖记录

每次采集把下列对象写入热点主文件的同名 `.coverage.json` sidecar，避免改变现有热点列表结构：

```json
{
  "checked_at": "ISO-8601",
  "available_channels": ["web", "github"],
  "failed_channels": [{"channel": "reddit", "reason": "login required"}],
  "fallbacks_used": [{"from": "twitter", "to": "rss"}]
}
```
