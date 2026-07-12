# 项目日志 · 一天一迭代

> 战略（2026-07-04 定）：**公众号连载为主，一天一更；书是最后的最后，把连载合并成书。**
> 每天记录：干了什么 / 产出 / 明天要干什么。

## Day 1 · 2026-07-04

**干了什么**
- 立项：蒸馏花叔（五步流水线/变现模型/空档确认），确认科研线空白
- 大纲 v0.2（10 章，案例占半）+ 生产手册 v0.1（先实测再写/章模板/独立拷打）
- md→PDF 产线搭通（pandoc + 无头 Chrome），试印大纲修掉 2 个排版 bug
- paper-search skill 出公开发行版（去个人信息、去灰色渠道、Windows 适配），入仓 `skills/`
- 写手 Agent 实测 §03 四步流程（OpenAlex 真数据）
- 公众号 Day 1 文章：软件介绍 + skill 开源 + 烧钱预警 + 实测案例

**产出**
- 仓库上线：github.com/Dalaoyuan2020/claude-science-green-book
- `articles/2026-07-04-day01.md`
- 进度面板 Artifact（链接见 RESUME.md）

**Day 1 追加（晚间）**
- §03 样章走完全产线：写手实测→成稿→独立拷打（P0=0）→一轮修订 15/15→PDF
- study-blog 开新系列「Claude Science 绿皮书」，第 1 篇《01 · Claude Science 是什么》已上线（精华版+封面），结尾埋两问题钩子
- MacBook 打通（IP 漂移改用主机名连），dev 预览服务起在 http://192.168.31.21:5173/study-blog/

**明天（Day 2）已定**
- 主题：怎么在 Windows 上用上 Claude Science（接今天结尾的两个问题之一）
- 公众号 Day 2 长文 + study-blog 第 2 篇精华版同步
- §03 样章 PDF 待吕博验收

## 2026-07-07 · Day 2 全线发布

- 原版定稿 `articles/2026-07-06-day02.md`（3683 字，去AI味 100/100）：四座山→CSA三件套→先装后用→注意事项，五图齐
- 精华版已上 study-blog（02-run-it-on-windows），公众号已发表（河小驴，摸鱼绿排版，图片全转存成功）
- 小红书 3 卡已发（Claude Science 星芒钩子/真机截图/绿皮书种草）
- 新增 `articles/assets/DESIGN_SPEC.md`（系列配图规范）+ 星空画芯 + HTML 模板产线
- 公众号排版产线建立（gzh-design-skill 摸鱼绿，校验 0 ERROR），流水线文档在本地 gzh/WORKSPACE.md
- ⚠️ 教训：公众号摘要/作者是独立字段，交付时必须显式提醒人工填
- 待办：CSA Release v0.1.1（吕博传 zip）；Day 3「30 分钟摸清一个方向」

## 2026-07-12 · Day 3 + Day 4 双章推送

**Day 3「打磨，打磨，再打磨」（v0.1.3 更新故事）**
- 原版 `articles/2026-07-12-day03.md`（去AI味 100/100）：C盘跑爆→磁盘体检 / DeepSeek方言冤案 / 订阅版vsAPI版两副面孔→主动性调回 / 升级一句话丢给AI
- 五图：老模板封面(03·千锤百炼) + 新界面截图 + 四打磨点 + 千锤百炼锻造图(gpt-image-2 版画风+HTML压字) + 真实会话产出(20篇文献综述)
- 精华版已上 study-blog（03-polish-polish-polish）；公众号排版 gzh/day03（0 ERROR）待发
- 配图产线升级：信息图走 HTML 渲染零AI感，趣味插画走 TOAPIS gpt-image-2（版画/水彩风、无文字防错字）

**Day 4「最省钱的用法」（OpenCode Go 国产性价比模型）**
- 原版 `articles/2026-07-13-day04.md`（去AI味 100/100）：初衷=一天一块二用上搭档 / OpenCode Go($5首月$10次月) / 主力选GLM-5.2 / 性价比≠将就(酶动力学R²0.9925+20篇综述拼图) / 邀请码+三要素收尾催动手
- 官方表述已核对对齐（opencode.ai/go：低成本编码模型人人可用 / 模型清单 / 价格）
- 四图：老模板封面(04·最省钱的用法) + 模型自助餐额度图 + 国产性价比模型成果拼图 + 三要素"就差你了"收尾图
- 邀请链接 opencode.ai/go?ref=7ZWT70EQ03（双方各返$5）

**README 挂工具**：中英文 README 封面下新增 CSA 配套工具入口（开源仓库 + Releases 下载）
- 待办：Day 4 精华版→阅读室；Day 3/Day 4 公众号定时发；小红书 Day 4 三卡+共用主视觉；CSA Release（吕博传 zip）
