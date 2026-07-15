#!/bin/bash
# Step 1: Pull literature on "lightweight industrial anomaly detection", 2021-2026
# OpenAlex API, free, no key. mailto param = polite pool (faster, more stable).
# Ran on 2026-07-04 by the ch03 writer agent.
#
# ---- ATTEMPT 1 (FAILED, kept as evidence of the pit) ----
# Plain `search=` matches loosely across all fields.
# Result: 25,331 hits, top ones were 6G / Metaverse / IoT surveys. Useless.
curl -s "https://api.openalex.org/works?search=lightweight%20industrial%20anomaly%20detection&filter=publication_year:2021-2026&sort=cited_by_count:desc&per-page=50&select=id,title,publication_year,cited_by_count,primary_location,type,keywords,concepts&mailto=your@email.com" \
  -o step1_response_wide_FAILED.json

# ---- ATTEMPT 2 (WORKS) ----
# Anchor the exact phrase in title+abstract, then OR the "lightweight" synonyms.
# Result: 269 hits, top ones are EfficientAD / PNI / FAPM etc. All on target.
curl -s 'https://api.openalex.org/works?filter=title_and_abstract.search:%22industrial%20anomaly%20detection%22%20AND%20(lightweight%20OR%20efficient%20OR%20real-time%20OR%20edge),publication_year:2021-2026&sort=cited_by_count:desc&per-page=50&select=id,title,publication_year,cited_by_count,primary_location,type,keywords&mailto=your@email.com' \
  -o step1_response.json

echo "--- wide (failed) ---"
jq '{total: .meta.count, returned: (.results | length)}' step1_response_wide_FAILED.json
echo "--- refined ---"
jq '{total: .meta.count, returned: (.results | length)}' step1_response.json
