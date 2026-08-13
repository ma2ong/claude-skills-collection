# 第三方来源与致谢

本仓库整体以 MIT 许可发布（见 `LICENSE`）。以下 skill 的方法论或依赖来自第三方，在此声明。

## khazix-writer — 方法论来源

`khazix-writer/` 的写作方法论（HKR 选题质检、五种内容原型、四层自检、"有见识的普通人在认真聊一件打动他的事"的定位）源自：

- **项目**：[KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)
- **作者**：数字生命卡兹克（KKKKhazix）
- **上游许可**：MIT

本仓库中的 `SKILL.md` 与 `references/` 为独立转写与精简，**未逐字复制上游文本**（三个文件与上游逐行比对，相同行数为 0）。方法论归属已在 `khazix-writer/SKILL.md` 的 frontmatter 中以 `source` / `author` 字段标注。

若你想要完整原版（含更长的风格示例库与更多 agent），请直接使用上游仓库。

## aihot — 第三方公开 API

`aihot/` 调用 [aihot.virxact.com](https://aihot.virxact.com) 的公开匿名只读 REST API 获取中文 AI 资讯。

- **API 与数据归属**：Virxact
- **本仓库提供的部分**：仅为调用约定与中文简报整理规则，不含任何数据
- **凭据**：该 API 匿名可访，无需 API Key

数据的可用性、准确性与服务条款由 Virxact 决定，本仓库不作担保。上游另有一个由 Virxact 作者维护的 aihot skill 收录在 khazix-skills 中，与本仓库的实现相互独立。

## 方法论影响

以下写作方法论对 `vibe-writer-pro` / `vibe-writer` 有影响，均为公开分享的思路，非代码或文本移植：MapleShaw 的自动化流程、花叔的审校架构、Baoyu 的视觉审美。

## 可选外部工具

部分 skill 在采集环节会调用以下工具，**均为可选**，缺失时按各自 SKILL.md 里的降级路径处理：

- `opencli` — 社交/内容站点的命令行访问
- `guizang-social-card-skill` — 社交卡片配图（`content-converter` 中作为推荐项提及）
