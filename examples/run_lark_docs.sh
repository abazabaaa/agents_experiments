#!/usr/bin/env bash
set -euo pipefail

# Default configuration targets the Lark documentation hosted on Read the Docs.
# Docs overview: https://lark-parser.readthedocs.io/en/stable/ citeturn0search5

BASE_URL=${BASE_URL:-"https://lark-parser.readthedocs.io/en/stable/"}
OBJECTIVE=${OBJECTIVE:-"Capture the full Lark documentation with emphasis on grammar syntax, parsing algorithms, and usage guidance."}
LOG_DIR=${LOG_DIR:-"logs"}
OUTPUT=${OUTPUT:-"artifacts/lark_docs.json"}
MAP_LIMIT=${MAP_LIMIT:-500}

mkdir -p "$LOG_DIR" "$(dirname "$OUTPUT")"

uv run scripts/trio_agents_firecrawl.py \
  --base-url "$BASE_URL" \
  --objective "$OBJECTIVE" \
  --log-file "$LOG_DIR/lark_docs.log" \
  --output "$OUTPUT" \
  --map-limit "$MAP_LIMIT" \
  --progress-interval 5 \
  --scrape-concurrency 3 \
  --thread-concurrency 8 \
  "$@"
