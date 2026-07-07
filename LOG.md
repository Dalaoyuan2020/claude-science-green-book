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
