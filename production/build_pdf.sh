#!/bin/bash
# 绿皮书 PDF 产线 v0.1：md → (pandoc) → HTML → (无头 Chrome) → PDF
# 用法: ./build_pdf.sh <输入.md> [输出名前缀]
# 版本号自动进文件名（学花叔 vYYMMDD），绝不手改产物。
set -euo pipefail

IN="$1"
NAME="${2:-$(basename "$IN" .md)}"
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT_DIR="$DIR/dist"
VER="v$(date +%y%m%d)"
mkdir -p "$OUT_DIR"

HTML="$OUT_DIR/${NAME}-${VER}.html"
PDF="$OUT_DIR/${NAME}-${VER}.pdf"

pandoc "$IN" \
  --standalone \
  --css "$DIR/book.css" \
  --embed-resources \
  --metadata title=" " \
  --from markdown+east_asian_line_breaks-smart \
  --to html5 \
  -o "$HTML"

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$PDF" \
  "file://$HTML" 2>/dev/null

echo "OK: $PDF"
