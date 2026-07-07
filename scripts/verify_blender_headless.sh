#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BLENDER_BIN="${BLENDER_BIN:-blender}"

if ! command -v "$BLENDER_BIN" >/dev/null 2>&1; then
  echo "BLENDER_NOT_FOUND: set BLENDER_BIN=/path/to/blender or add blender to PATH" >&2
  exit 2
fi

"$BLENDER_BIN" --background --python "$ROOT/scripts/create_blender_smoke_scene.py"
python3 - <<PY
from pathlib import Path
p = Path(r"$ROOT") / "build" / "blender" / "smoke_scene.glb"
print({"exists": p.exists(), "size": p.stat().st_size if p.exists() else 0, "path": str(p)})
raise SystemExit(0 if p.exists() and p.stat().st_size > 1000 else 1)
PY
