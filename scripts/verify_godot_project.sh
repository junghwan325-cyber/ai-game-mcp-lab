#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT="${1:-$ROOT/godot/coin-runner}"
GODOT_BIN="${GODOT_BIN:-godot4}"

if ! command -v "$GODOT_BIN" >/dev/null 2>&1; then
  echo "GODOT_NOT_FOUND: set GODOT_BIN=/path/to/godot4 or add godot4 to PATH" >&2
  exit 2
fi

LOG="$ROOT/build/godot-load.log"
mkdir -p "$(dirname "$LOG")"
"$GODOT_BIN" --headless --path "$PROJECT" --quit --verbose >"$LOG" 2>&1 || {
  tail -160 "$LOG"
  exit 1
}
echo "GODOT_PROJECT_LOAD_OK"
"$GODOT_BIN" --version
