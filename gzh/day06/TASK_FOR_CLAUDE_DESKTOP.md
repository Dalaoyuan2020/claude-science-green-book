# 任务：把绿皮书第 6 篇（设置中心）发布任务提炼成执行 Prompt

> 你是 Claude 桌面版。把下面的「发布任务」提炼成一段完整、自包含、可直接粘贴给执行 agent（Claude Work / Codex）的 Prompt。执行 agent 看不到本文件，所有路径、文案、步骤、红线都要写全。

## 发布任务

把已排版好的公众号文章上传到微信公众平台，**保存为草稿**（不群发）。

### 素材

- 正文 HTML（已按公众号规范排版并校验 0 ERROR）：
  `~/Documents/Claude_Mini_agent/claude-science-green-book/gzh/day06/day06精华版_排版_摸鱼绿(moyu-green).html`
- 一键复制预览页（浏览器打开，右上角「复制到公众号」按钮）：
  `~/Documents/Claude_Mini_agent/claude-science-green-book/gzh/day06/day06精华版_排版_摸鱼绿(moyu-green)_预览.html`
- 封面图（1:1，方案 A 上手绿 + 星空画）：
  `~/Documents/Claude_Mini_agent/claude-science-green-book/articles/assets/day06/cs06-cover.png`

### 发布信息

- 标题：`Day 6 · Claude Science 设置中心`
- 作者：`河小驴`
- 摘要：`左下角齿轮进去，十一个面板：上面给它加本事，下面管住它。开箱真正要动的就四条。`
- 原文链接（若编辑器支持）：`https://dalaoyuan2020.github.io/study-blog/reading/claude-science/06-settings-center`

### 执行步骤

1. 浏览器打开 `mp.weixin.qq.com`（已登录；掉登录就停下让用户扫码，不代登录）
2. 新建图文消息
3. 打开预览页，点右上角「复制到公众号」，回编辑器正文区粘贴
4. 核对正文：图是否全部转存成功（**共 15 张**：封面图 + 入口 + 侧栏 + Skills + Connectors + Specialists + Memory + Compute + Network + Permissions + Credentials + Storage + Usage + General + 结尾总结图，均来自 study-blog 直链）；排版是否与预览一致；裂了就手动上传替换
5. 填标题、作者、摘要，上传封面图（2.35:1 裁切保持画面居中）
6. **保存为草稿，到此为止**。不群发、不发表、不改账号设置
7. 回报：草稿链接/截图 + 哪些图自动转存/哪些需人工

### 红线

- 只存草稿，**严禁群发/发表**（群发由用户人工点）
- 不改公众号任何设置
- 登录态缺失停下问用户，不代登录
- 遇验证码/风控立即停下报告

## 你的输出格式

直接输出提炼后的 Prompt 正文（含全部路径与红线），不要附加解释。
