# 公众号发布前体检 + 故障排查（Preflight Runbook）

> 解决的不是"写得好不好"，是**最后一公里能不能稳定进草稿箱、进去之后排版图片对不对**。
> 核心原则：**发布前检查 > API 重试**。多数失败不是代码 bug，是配置/白名单/图片/调用顺序。**拿不到 `media_id` 不算成功**——接口没抛异常 ≠ 发布成功。

## 三段式发布顺序（不能混）

正文图、封面图、草稿创建是三层，分开处理：

1. **token** → 拿 `access_token`
2. **正文图上传** → 每张图换成微信永久素材 URL（`mmbiz.qpic.cn` 域名）
3. **封面图上传** → 拿 `thumb_media_id`（草稿字段依赖）
4. **草稿创建** → `add_draft`，成功条件 = 返回 `media_id`

## 发布前 7 项硬检查（任一不过就别推，先修）

| # | 检查项 | 不过的后果 | 怎么修 |
|---|---|---|---|
| 1 | **正文图全部素材化** | 外链图被微信过滤 → 正文图全丢 | 每张图先 `upload_img` 换 `mmbiz.qpic.cn` URL，再插进 HTML。绝不直接引用外链/本地路径 |
| 2 | **封面 `thumb_media_id` 已设** | `add_draft` 报错或无封面 → 推送失败 | 先传封面拿 thumb_media_id 再建草稿 |
| 3 | **无深色背景 + 白字组合** | 微信编辑器剥离深色背景 → 白字在白底上不可见 | 全程深色文字 + 浅色背景。扫描 HTML 里 `background:#[深色]` 配 `color:#fff/#fff` 的段落 |
| 4 | **标题 ≤ 64 字 / 摘要 ≤ 120 字** | 超长被截断或报错 | 截断前确认钩子在前 13 字（见 `title_formulas.md`） |
| 5 | **IP 白名单已配** | token 接口报 `40164 invalid ip` | 公众号后台 → 基本配置 → IP 白名单加当前出口 IP |
| 6 | **appid/secret 有效** | `40013 invalid appid` / `40001 secret` | 查 `xiaohu-wechat-format/config.json`，确认没过期、没填错 |
| 7 | **表格/复杂排版降级** | 微信吃不下复杂 table，错位 | 「明天看什么」这类用普通段落，不用 table（已知踩坑） |

## 常见 errcode 速查

| errcode | 含义 | 处理 |
|---|---|---|
| 40001 | secret 错或 token 过期 | 重新拿 token；查 secret |
| 40013 | appid 无效 | 查 config.json |
| 40164 | IP 不在白名单 | 后台加白名单 |
| 41005 | 缺媒体文件 | 封面/正文图没传成功 |
| 45009 | 接口调用超频 | 等一会儿；别循环重试 |
| 53400 | 草稿字段不全 | 多半是 thumb_media_id 缺失 |

## 降级原则：缺条件就诚实 preview，不伪造成功

如果没凭据 / 白名单没配 / 图片条件不成立 → 生成**本地 HTML preview** 并明确告诉用户：

- 失败发生在哪一步
- 关键 errcode / errmsg（原样保留，不做模糊报错）
- 已生成本地 preview 路径
- 还缺什么配置或人工动作

**绝不**因为"接口没报错"就告诉用户"发布成功了"。

## Allen 的现成实现（优先复用，别重造轮子）

发布前先看仓库里有没有能直接用的：

- `md2wechat-skill`：`bash skill/md2wechat/scripts/run.sh convert article.md --draft --cover cover.jpg`（Go 实现，含 API/AI 双模式 + 图床）
- `xiaohu-wechat-format`：凭证在 `config.json`（appid/secret）
- `build_draft.js` / `push_stock_review_draft.py`：已验证可用的推草稿脚本

> 方法论：**先看有没有现成实现，再决定改什么。** 公众号发布最容易重复造轮子，仓库里已有稳定实现优先复用，只做发布必需的最小修正，不顺手改正文。
