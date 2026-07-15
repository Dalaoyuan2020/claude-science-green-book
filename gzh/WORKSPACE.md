# 公众号发布流水线 · 工作区文档

> 目标：公众号文章从排版到发布全自动化。本文件是流水线的单一说明书，任何 agent 接手先读这里。
> 建立：2026-07-07 · Napoleon

## 工作区路径

```
~/Documents/Claude_Mini_agent/claude-science-green-book/gzh/
├── WORKSPACE.md                 ← 本文件（流水线说明书）
└── day02/                       ← 每期一个文件夹（day03、day04…同结构）
    ├── day02精华版_排版_摸鱼绿(moyu-green).html    ← 干净正文（校验过，手动兜底用）
    ├── day02精华版_排版_摸鱼绿(moyu-green)_预览.html ← 带「复制到公众号」按钮的预览页
    └── TASK_FOR_CLAUDE_DESKTOP.md                  ← 给 Claude 桌面版的任务文件
```

## 三步流水线（吕博 2026-07-07 定）

| 步 | 谁执行 | 干什么 | 状态 |
|---|---|---|---|
| ① 本地排版 | Napoleon（本机 Claude Code） | 用 gzh-design-skill（摸鱼绿主题）把精华版 Markdown 排成公众号 HTML，校验 0 ERROR，产物存本地 | ✅ Day 2 已完成 |
| ② 任务提炼 | Claude 桌面版 | 读 `dayNN/TASK_FOR_CLAUDE_DESKTOP.md`，把任务提炼成一段给执行 agent 的发布 Prompt | ⏳ 待吕博喂给桌面版 |
| ③ 自动发布 | Claude Work / Codex | 拿着②的 Prompt 操作 mp.weixin.qq.com：新建图文 → 粘贴 → 设标题/作者/封面/摘要 → **只存草稿** | ⏳ |

**安全闸门：③只保存草稿，绝不直接群发。群发永远由吕博人工点。**

## 关键约定

- **排版源**＝精华版（吕博定：公众号排精华版）；内容真理源在 `articles/`（原版）与 study-blog（精华版），排版不改内容
- **排版技术**＝gzh-design-skill（github.com/isjiamu/gzh-design-skill 蒸馏），主题＝摸鱼绿（#059669，贴绿皮书品牌绿；教程类推荐主题）
- **平台红线**＝样式全内联、文字全 `<span leaf>` 包裹、禁 div/class/style 标签；校验脚本 0 ERROR 才算完成
- **图片**＝引用 GitHub Pages 直链（https://dalaoyuan2020.github.io/study-blog/day02-*.png），公众号编辑器粘贴时会自动转存；若个别图转存失败，人工上传素材库替换
- **手动兜底**＝浏览器打开 `_预览.html` → 点右上角「复制到公众号」→ 编辑器 ⌘+V 粘贴
- **⚠️ 发布前人工三件套（2026-07-07 Day 2 教训：摘要/作者漏填了）**＝粘贴只解决正文，**摘要、作者、封面图**是编辑器侧边的独立字段，必须人工填。Napoleon 每次交付排版产物时，要在结尾显式提醒这三样，并把现成文案贴出来供复制

## Day 2 发布信息（✅ 已发表 2026-07-07）

- 标题：`Day 2 · Windows 用不了？我们直接做了个双击就能用的`
- 作者：`河小驴`
- 摘要：`双击一个图标，把 Claude Science 跑起来；还能接国产模型省饭钱。`
- 封面：`articles/assets/day02/img1-cover-csa.png`（1:1 星空封面；2.35:1 用编辑器居中裁切）
- 原文链接（可选）：`https://dalaoyuan2020.github.io/study-blog/reading/claude-science/02-run-it-on-windows`

## Day 3 发布信息（③要用）

- 标题：`Day 3 · 我把自己的 C 盘跑爆了，然后有了这次更新`
- 作者：`河小驴`
- 摘要：`三个真实的坑，四个打磨点。CSA v0.1.3：从「能跑通」，磨到「真的可用」。`
- 封面：`articles/assets/day03/img1-cover-classic.png`（1:1 星空模板；2.35:1 用编辑器居中裁切）
- 原文链接（可选）：`https://dalaoyuan2020.github.io/study-blog/reading/claude-science/03-polish-polish-polish`
- 排版产物：`gzh/day03/`（正文 HTML 0 ERROR ✅ + 预览页 + 桌面版任务文件）
