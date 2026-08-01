# 番外01 发布 · 任务拆解 prompt（本地执行用）

> 源稿：`claude-science-green-book/articles/extra01-preview.html`（已本地预览定稿）
> 图片：`claude-science-green-book/articles/assets/extra01/`（9 张）
> 铁则：不重写全文；不改任何数字；术语只用 Claude Science / V4 Flash / 脑手眼三层。

---

## 任务 A · 推阅读室（study-blog）—— 详细版

**目标**：把番外01 挂到 study-blog 阅读室，作为公众号版的取稿源。阅读室版是**最全的详细版**。

1. **建正文页** `study-blog/reading/claude-science/extra01-deepseek-v4-flash.md`：
   - frontmatter 给独立 `pageClass: extra01`（视觉只作用本页，不污染其它文章）
   - 标题：`DeepSeek V4 Flash 实测：8 块钱跑完一个完整任务`；byline `Claude Science 绿皮书 · 番外 01 · 2026-08-01`
   - 正文以预览页全文为准（**比公众号详细**）：省流 → 一(GLM 痛点+成本图) → 二(V4 发布+性能对比+价格表+价格线) → 三(账单 70M/¥8.48/681次) → 四(不断) → 五(瞎子) → 六(脑手眼+分层图) → 七(案例 3 图：样本/AUROC/热力图) → 总结表 → 复盘 → 一句带走 → 邀请码卡片（原样保留）
   - 图注带「图 N：」编号（正文 8 张 + 封面），图、表全保留，9 张图一张不删
2. **图片落位**：把 `assets/extra01/*.png`（9 张）拷到 `study-blog/public/claude-science/extra01/`，md 里引用 `/claude-science/extra01/<名>.png`
3. **页面级 CSS**：`study-blog/.vitepress/theme/custom.css` 追加 `.extra01` 作用域块——配图块级居中、近方形图（bill 1014×971）适当收窄、图注居中弱化、表格可横向滚动
4. **侧边栏**：`.vitepress/config.mts` 在绿皮书系列 09 之后加 `{ text: '番外 · 8 块钱的一夜（DeepSeek V4 Flash）', link: '/reading/claude-science/extra01-deepseek-v4-flash' }`
5. **构建 + 自检**：`npm run build` 通过；图全 200、表格在、无裸公式、邀请码在
6. **提交**：`git add` 仅指定路径（新 md、9 张图、config.mts、custom.css），**绝不 `git add .`**（防 `.bak2` 混入），单次 commit + push `main`，等 Actions 部署，线上复核

---

## 任务 B · 转公众号（gzh-design）—— 内容量保持现版

**目标**：把阅读室这篇转成可直接粘贴的公众号 HTML。**内容量就用现在这版，不再额外压缩**（吕博：目前这个量够）。

1. **主题**：摸鱼绿（与 day02–day09 系列一致，主色 `#059669`）
2. **源**：阅读室 md / 预览页全文，**不砍内容**；9 张图全保留
3. **图片用线上外链**：任务 A 推完后，图地址为 `https://dalaoyuan2020.github.io/study-blog/claude-science/extra01/<名>.png`（逐张 curl 复验 200）
4. **排版**：读 `references/theme-moyu-green.md` + `common-components.md`，按教程/案例复盘配方装配；每段主动标 1–3 个下划线关键词；章节自动编号 + 英文标签；封面卡 + 目录卡 + 引言卡 + 签名区
5. **署名**：**河小驴**（绝不出现 Winnie/羊爸爸/博士/订阅）
6. **邀请码卡片**：作为结尾 CTA 区原样保留（链接+邀请码不动）
7. **校验**：`validate_gzh_html.py` 跑到 **0 ERROR + 0 WARNING**（含半角标点清零）；禁 div/class/style 标签、全内联、`<span leaf>` 包裹、图 `max-width:100%`
8. **产物**：`gzh/extra01/extra01_排版_摸鱼绿(moyu-green).html` + `_预览.html`（wrap_preview.py 生成，带复制按钮）
9. **交付**：告知「打开预览页 → 点复制 → 公众号编辑器粘贴」，附校验结论 + 图清单
