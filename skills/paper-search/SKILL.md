---
name: paper-search
description: 学术论文检索与获取。当用户说"找文章/找论文/查文献/找相关工作/帮我搜XX方向的论文/给我XX方向的参考文献"，或论文写作需要文献支撑时触发。OpenAlex 主力检索（免费免 key）+ Semantic Scholar 补充 + 开放获取（OA）全文优先下载。
version: 1.1.0-public
---

# Paper Search · 学术论文检索获取（公开版）

用户说"找文章/查文献/找相关工作"时用本 skill。流程：搜索 → 给排名清单 → 按需下全文。
Windows / Mac / Linux 通用，只依赖 Python 标准库，不需要装任何第三方包。

## 0. 安装（一次性）

把本文件夹放到 Claude Code 的 skills 目录：

- **Windows**: `C:\Users\你的用户名\.claude\skills\paper-search\`
- **Mac/Linux**: `~/.claude/skills/paper-search/`

然后把 `scripts/oa_search.py` 里的 `your-email@example.com` 改成你自己的邮箱（OpenAlex 礼貌池，填了更快更稳）。

## 1. 搜索（主力 OpenAlex，免费免 key）

```bash
# Windows 用 python，Mac/Linux 用 python3
python scripts/oa_search.py "你的检索词(英文最佳)" --limit 8 --sort cites
# --sort: cites(引用排序,找经典) / year(最新) / rel(相关性,默认)
# --year-from 2022  只看近几年
# --oa-only         只看有免费全文的
```

输出：标题 / 年份 / 引用数 / DOI / OA 状态 / 免费 PDF 链接 / 摘要片段。

## 2. 搜索补充（Semantic Scholar，有 TL;DR）

```bash
curl -s --max-time 20 "https://api.semanticscholar.org/graph/v1/paper/search?query=QUERY&limit=5&fields=title,year,citationCount,externalIds,openAccessPdf,tldr"
```

⚠️ 没 API key 时经常限流（返回空或 429）。要稳定用，去 semanticscholar.org/product/api 申请免费 key。OpenAlex 够用就别依赖它。

## 3. 下全文（只走合法渠道）

1. **OpenAlex 给的免费 PDF 链接** —— 直接下载，合法免费
2. **Unpaywall** 再找一次开放版本：
   `curl -s "https://api.unpaywall.org/v2/{DOI}?email=你的邮箱"` → 取 `best_oa_location.url_for_pdf`
3. 都没有 → 记下 DOI，通过学校图书馆数据库获取，或邮件向通讯作者索取（学界惯例，成功率不低）

## 4. 输出格式

排名清单，每篇一行：`序号. 标题 (年) | 引用N | DOI | [免费PDF: 有/无]`，附一句摘要要点。问用户要哪几篇下全文，再下。

## 5. 用法要点

- 检索词用**英文**（覆盖最全）；中文主题先转英文关键词
- 找经典基础用 `--sort cites`；找最新进展用 `--year-from 2024 --sort year`
- 写论文找"相关工作"时：搜同主题 → 按引用排 → 挑高引经典 + 近 2 年新作
- 数据真实：OpenAlex 是真 API，不编造文献；找不到就说找不到，**AI 报的每条文献都应核对 DOI 真伪**
