#!/usr/bin/env python3
"""OpenAlex 论文检索 (主力, 免key). 用法:
  python3 oa_search.py "query" [--limit N] [--year-from YYYY] [--oa-only] [--sort cites|year|rel]
输出: 排名 标题/年/引用/DOI/OA/OA_PDF/摘要片段
"""
import sys, json, urllib.parse, urllib.request, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--limit", type=int, default=8)
    ap.add_argument("--year-from", type=int)
    ap.add_argument("--oa-only", action="store_true")
    ap.add_argument("--sort", choices=["cites","year","rel"], default="rel")
    a = ap.parse_args()

    filt = []
    if a.year_from: filt.append(f"from_publication_date:{a.year_from}-01-01")
    if a.oa_only: filt.append("is_oa:true")
    sort = {"cites":"cited_by_count:desc","year":"publication_date:desc","rel":"relevance_score:desc"}[a.sort]
    params = {"search": a.query, "per-page": a.limit, "sort": sort,
              "mailto": "your-email@example.com"}
    if filt: params["filter"] = ",".join(filt)
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=25) as r:
            d = json.load(r)
    except Exception as e:
        print("OPENALEX_ERROR:", e); sys.exit(1)

    print(f"# OpenAlex: \"{a.query}\"  命中 {d.get('meta',{}).get('count')} 篇, 取前 {a.limit}\n")
    for i, w in enumerate(d.get("results", []), 1):
        oa = w.get("open_access", {})
        doi = (w.get("doi") or "").replace("https://doi.org/", "")
        # 重建摘要(OpenAlex 是倒排索引)
        ab = w.get("abstract_inverted_index")
        snip = ""
        if ab:
            words = [None]*(max(p for ps in ab.values() for p in ps)+1)
            for word, ps in ab.items():
                for p in ps: words[p] = word
            snip = " ".join(w for w in words if w)[:200]
        print(f"{i}. {w.get('title')}  ({w.get('publication_year')}) | 引用 {w.get('cited_by_count')}")
        print(f"   DOI: {doi or '—'} | OA: {oa.get('is_oa')} | OA_PDF: {oa.get('oa_url') or '—'}")
        if snip: print(f"   摘要: {snip}…")
        print()

if __name__ == "__main__":
    main()
