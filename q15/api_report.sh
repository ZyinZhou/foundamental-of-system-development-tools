#!/usr/bin/env bash
set -e

# 1. curl获取本地服务JSON，jq筛选排序
curl -fsS http://127.0.0.1:8000/packages.json | jq '
    map(select(.status=="active" and .downloads >= 100))
    | sort_by(-.downloads, .name)
' > filtered.json

# 2.输出summary.md
cat > summary.md <<EOF
# Package Summary Report

| name | version | downloads |
|------|---------|-----------|
EOF

# jq -r 输出原始文本，循环写入表格行
jq -r '.[] | "| \(.name) | \(.version) | \(.downloads) |"' filtered.json >> summary.md

