#!/usr/bin/env python3
# Steps 2+3: build the "schools map" and the 4-dimension stats
# from the real OpenAlex response (step1_response.json).
# Ran on 2026-07-04 with /usr/bin/python3. Zero third-party deps.
import json, re, collections

with open("step1_response.json") as f:
    data = json.load(f)
works = data["results"]
print(f"works loaded: {len(works)}\n")

# ---------- Step 2: bucket into schools by title keywords ----------
# Rules written AFTER eyeballing the real titles (not from prior knowledge).
RULES = [
    ("蒸馏/师生网络",  r"teacher|student|distill"),
    ("记忆库/特征嵌入", r"memory|patch\s?core|patchcore|neighborhood|softpatch|tiled"),
    ("重建/生成类",    r"reconstruct|autoencoder|auto-encoder|inpaint|gan\b|restoration|generative"),
    ("归一化流",       r"normalizing flow|uniflow|\bflow\b"),
    ("大模型/零样本",   r"clip|sam-|vision-language|zero-shot|foundation"),
    ("多模态/3D",     r"multimodal|multi-modal|3d|rgb-d|cross-modal|point cloud"),
    ("时序/IoT 传感",  r"time.?series|time series|lstm|iot|sensor|robotic arm|edge devices"),
]
buckets = collections.defaultdict(list)
for w in works:
    t = (w["title"] or "").lower()
    placed = False
    for name, pat in RULES:
        if re.search(pat, t):
            buckets[name].append(w["title"])
            placed = True
            break  # first match wins to keep counts disjoint
    if not placed:
        buckets["其他(检测头/框架/综述等)"].append(w["title"])

print("=== Step 2: 流派分桶 (title-rule based, first-match-wins) ===")
for name, items in sorted(buckets.items(), key=lambda kv: -len(kv[1])):
    print(f"\n[{name}] {len(items)} 篇")
    for t in items:
        print(f"  - {t}")

# ---------- Step 3: 4-dimension stats ----------
print("\n=== Step 3.1: 年份分布 ===")
years = collections.Counter(w["publication_year"] for w in works)
for y in sorted(years):
    print(f"{y}: {'#' * years[y]} {years[y]}")

print("\n=== Step 3.2: 来源 Top (primary_location.source) ===")
venues = collections.Counter(
    (w.get("primary_location") or {}).get("source", {} ) and
    ((w.get("primary_location") or {}).get("source") or {}).get("display_name", "unknown")
    or "unknown"
    for w in works
)
for v, c in venues.most_common(10):
    print(f"{c}  {v}")

print("\n=== Step 3.3: 高频关键词 (OpenAlex keywords 字段) ===")
kws = collections.Counter()
for w in works:
    for k in (w.get("keywords") or []):
        kws[k["display_name"]] += 1
for k, c in kws.most_common(15):
    print(f"{c}  {k}")

print("\n=== Step 3.4: 内容构成 (type + 标题启发式) ===")
types = collections.Counter(w["type"] for w in works)
print("OpenAlex type:", dict(types))
kind = collections.Counter()
for w in works:
    t = (w["title"] or "").lower()
    if re.search(r"survey|review|overview", t):
        kind["综述类"] += 1
    elif re.search(r"application|packaged food|cigarette|smart cities|appliance|robotic arm|x-ray", t):
        kind["应用类"] += 1
    else:
        kind["方法类"] += 1
print("标题启发式:", dict(kind))
