# 本地 skill 安装说明

本目录下的 skill **不进 git**（见仓库 `.gitignore`），换机器或重新 clone 后需要重装。

## gzh-design（公众号排版 SOP）

公众号排版的唯一标准。**不许凭记忆手写组件，不许照着上一期成品反推。**

```bash
# 在仓库根目录执行
git clone --depth 1 https://github.com/isjiamu/gzh-design-skill.git .claude/skills/gzh-design
rm -rf .claude/skills/gzh-design/.git
```

### 为什么不提交进仓库

| | 授权 |
|---|---|
| 绿皮书本体 | CC BY-NC-SA 4.0（非商业 · 相同方式共享） |
| gzh-design-skill | AGPL-3.0（允许商业，**禁止附加额外限制**） |

AGPL 不允许在其之上叠加「非商业」这类限制。把它提交进标着 NC 的公开仓库会造成授权冲突，
所以只在本地安装、用完即走。原作者：甲木（Jiamu）× 摸鱼小李（Moyu Xiaoli）。

### 排版怎么用

```bash
S=.claude/skills/gzh-design

# 1. 读 SOP 和主题库（HTML 一律从组件库取）
#    $S/SKILL.md               流程与决策
#    $S/references/theme-moyu-green.md   摸鱼绿组件库（本书固定用这套，#059669）
#    $S/references/common-components.md  代码块/图片/标签（所有主题共用）

# 2. 排版产物写好后，强制校验（ERROR 和 WARNING 都要清零）
/usr/bin/python3 $S/scripts/validate_gzh_html.py "gzh/dayNN/dayNN精华版_排版_摸鱼绿(moyu-green).html"

# 3. 生成带「复制到公众号」按钮的预览页
/usr/bin/python3 $S/scripts/wrap_preview.py "gzh/dayNN/dayNN精华版_排版_摸鱼绿(moyu-green).html"
```

### 2026-07-15 踩过的坑（Day 6 返工记录）

SOP 当时不在本机，照着 day04 成品反推，结果：

- 漏了 **正文每段标 1–3 个关键词下划线**（组件 6e）—— 这是该 skill 的核心特色，一个都没标
- 封面、目录、章节标题全自制，没用 cover-breaking / toc-scroll / chapter-title 组件
- 图片用了 `width:100%`（正确是 `max-width:100%`，否则小图被拉糊）
- 锚点层（绿色加粗 6a / oneliner-card 9b）撒得到处都是，规矩是**全文 ≤ 5 处**
- 结尾漏了 footer-cta 三连区
- 校验标准是我自己编的，没跑官方脚本

另一类坑：**规则和组件设计打架时，看组件实际怎么设计的**。
死抠 SKILL.md「目录取前 3 个」，但 toc-scroll 是横向滚动组件（注释写着「后续章节按需重复」），
六节的文章就该全列。**目录必须跟正文章节逐条对应，写脚本比对，别目测。**
