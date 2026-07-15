# 接力卡 · Claude Science 绿皮书

> 定向四问：我在哪 / 已完成 / 易错 / 下一步。任何 agent 接手先读这张卡。

## 我在哪

《Claude Science 绿皮书 · 科研实战》，Winnie lyu 著。对标花叔橙皮书系列（12 本全在 AI 编程线，科研线空白），我们打科研空档。本仓库 = 书稿真理源，GitHub 边写边推。

## 已完成（更新至 2026-07-15 · Day 6）

**连载已产出 6 篇**（每篇 = 公众号长文 + 阅读室精华版 + 小红书卡片）：

| Day | 主题 | 状态 |
|---|---|---|
| 1 | Claude Science 是什么 | ✅ 已发（小红书待补） |
| 2 | Windows 用不了？双击就能用 | ✅ 全渠道已发 |
| 3 | 打磨再打磨 · v0.1.3 | ✅ 全渠道已发 |
| 4 | 最省钱的用法 · OpenCode Go | ✅ 全渠道已发 |
| 5 | 框架介绍：一层层看懂这个软件 | ✅ 全渠道已发 |
| 6 | 设置中心：调成你自己的工作台 | ✅ 阅读室已发；公众号三件套待发 |

其它：
- ✅ 花叔蒸馏 `distill/huashu-distill.md`、双语 README + 封面、GitHub 仓库
- ✅ 公众号排版流水线（`gzh/`，摸鱼绿主题，每期一个文件夹）
- ✅ 界面素材库 `manuscript/source/interface-guide/`（17 张原图 + 发布用图 + 对应表，已脱敏）
- ✅ 方案 A「一脉青绿」配色分部：第二部上手篇 = 05、06

**目标：发到第 10 章算一个完整阶段**（吕博 2026-07-15 定）。

## 易错

- **公众号排版必须走 SOP，不许凭记忆手写**：SOP＝`github.com/isjiamu/gzh-design-skill`（摸鱼绿主题）。
  它**不在本机**，得先拉。2026-07-15 栽过：照着上一期成品反推，结果漏了「每段标 1–3 个关键词下划线」这个核心特色、封面/目录/章节组件全自制、图片用了 `width:100%`、校验标准自己编。
  产物必须跑该 skill 的 `scripts/validate_gzh_html.py`，**ERROR 和 WARNING 都清零**。
- **规则和组件设计打架时，看组件实际怎么设计的**。2026-07-15 连栽两次：死抠 SKILL.md「目录取前 3 个」，可 toc-scroll 是横向滚动组件（注释写着「后续章节按需重复」），六节的文章就该全列。目录必须跟正文章节逐条对应，**写脚本比对，别目测**。
- **本仓库是 PUBLIC**：截图入库前必须脱敏，台账见 `manuscript/source/interface-guide/image-map.md`。
- **术语别造比喻**：绿皮书偏学术，用软件原词（Capabilities＝能力配置 / Workspace＝工作区设置）。2026-07-15 造过「给它加本事」被否，又矫枉过正滑到大白话再被否。
- **数值必标出处**（真值/估/算/占位）；写的 agent 不审自己的稿。
- 别手写生成物：面板、阅读页都走脚本生成。
- 对外文案人话优先，黑话必须注解（GLOSSARY 规则）。

## 下一步

1. **Day 6 公众号发布**：三件套在 `gzh/day06/`，走桌面版存草稿 → 人工点发
2. **Day 6 小红书**：参考 `xhs/day05/` 的 6 卡系统贴形态
3. **Day 7 选题待议**：吕博 2026-07-15 提「介绍新功能」，具体内容待讨论
4. 拍板：`gzh-design-skill` 是否正式装到 `~/.claude/skills/gzh-design/`
5. ⚠️ **`OUTLINE.md` 已与实际连载脱节**：那是 2026-07-04 的成书大纲 v0.2（10 章，上手篇/武器篇/案例篇），跟 Day 1–6 的实际主线（介绍 → 装上 → 省钱 → 界面 → 设置）对不上。要么重写大纲对齐连载，要么明确「连载 ≠ 成书目录」。**待吕博定**

## 进度面板

- Artifact 地址（固定，重部署不换链接）：https://claude.ai/code/artifact/6cf052a7-d3ed-4763-b00c-cb4d22d74882
- 源文件在会话 scratchpad `greenbook-panel.html`；跨会话更新时用 Artifact 工具带 `url` 参数重部署
- 定向四问结构（我在哪/流水线/十章看板/已完成+易错+下一步），进度变了就更新重发

## 双版本规矩（2026-07-05 吕博定）

- 每篇内容两个版本：**原版**（公众号长文，`articles/`）+ **精华版**（博客章节版，study-blog）
- **真理源唯一**：内容修改只改原版，精华版由原版蒸馏同步，禁止两边各改各的（Day 1 漂移过一次）
- 吕博审美基线：**精华版的密度是标准**，原版也不许灌水——"废话太多真没人看"
- 改动流程照 [[confirm-before-push]]：先贴改动给吕博批，批了才推

## 素材指针

- SR-DDPM 全程案例：paper-git 仓库 + `project_srddpm_ijabe_20260607` 记忆
- 工具链原型：paper-search / paper-git / reviewer / ref-check / ijabe-cite / lit-analysis 各 skill
- 投稿体检 9 项：`reference_presubmission_checklist`
- 流程复盘六条铁律：`reference_paper_workflow_retro`
