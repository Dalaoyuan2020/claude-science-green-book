# 任务：把绿皮书 Day 3 发布任务提炼成执行 Prompt

> 你是 Claude 桌面版。请读完本文件，把下面的「发布任务」提炼成**一段完整、自包含、可直接粘贴给执行 agent（Claude Work 或 Codex）的 Prompt**。执行 agent 看不到本文件，所以你的 Prompt 必须把所有路径、文案、步骤、红线写全。

## 发布任务

把已排版好的公众号文章上传到微信公众平台，**保存为草稿**（不群发）。

### 素材（全部在本机）

- 正文 HTML（已按公众号规范排版并校验通过，0 ERROR）：
  `/Users/minilyu/Documents/Claude_Mini_agent/claude-science-green-book/gzh/day03/day03精华版_排版_摸鱼绿(moyu-green).html`
- 一键复制预览页（浏览器打开，右上角「复制到公众号」按钮，等价全选复制渲染后富文本）：
  `/Users/minilyu/Documents/Claude_Mini_agent/claude-science-green-book/gzh/day03/day03精华版_排版_摸鱼绿(moyu-green)_预览.html`
- 封面图（1:1 星空模板）：
  `/Users/minilyu/Documents/Claude_Mini_agent/claude-science-green-book/articles/assets/day03/img1-cover-classic.png`

### 发布信息

- 标题：`Day 3 · 我把自己的 C 盘跑爆了，然后有了这次更新`
- 作者：`河小驴`
- 摘要：`三个真实的坑，四个打磨点。CSA v0.1.3：从「能跑通」，磨到「真的可用」。`
- 原文链接（若编辑器支持）：`https://dalaoyuan2020.github.io/study-blog/reading/claude-science/03-polish-polish-polish`

### 执行步骤（提炼进 Prompt 时保留全部要点）

1. 用浏览器打开 `mp.weixin.qq.com`（用户浏览器已登录公众号后台；若掉登录，停下来让用户扫码，不要代操作登录）
2. 新建图文消息
3. 打开上面的「一键复制预览页」，点右上角「复制到公众号」按钮，回到编辑器正文区粘贴
4. 核对正文：图片是否全部转存成功（封面卡小图＋新界面截图＋千锤百炼图，共 3 张）；排版是否与预览页一致；若个别图裂了，从本机 `claude-science-green-book/articles/assets/day03/` 手动上传替换
5. 填标题、作者、摘要，上传封面图（2.35:1 裁切时保持星空画芯居中）
6. **保存为草稿，到此为止**。不点群发、不点发表、不改账号任何设置
7. 回报：草稿链接或截图 + 哪些图片被自动转存/哪些需人工处理

### 红线（原样写进 Prompt）

- 只存草稿，**严禁群发/发表**——群发由用户人工执行
- 不修改公众号任何设置（自动回复、菜单、白名单等一概不碰）
- 登录态缺失时停下来问用户，不尝试任何方式代登录
- 遇到验证码/风控提示，立即停下来报告

## 你的输出格式

直接输出提炼后的 Prompt 正文（一段完整指令，含全部路径与红线），不要附加解释。
