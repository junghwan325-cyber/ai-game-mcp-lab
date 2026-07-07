# Workflow

## Local iteration

1. Write or adapt a prompt in `prompts/`.
2. Generate a Blender asset with a local script or a local-only Blender MCP server.
3. Export GLB/GLTF into `build/` or `exports/`.
4. Import or reference the asset from a Godot project.
5. Run a headless Godot load check.
6. Only then open the editor for visual polish.

## Suggested verification commands

```bash
python3 -m unittest discover -s tests -v
scripts/verify_blender_headless.sh
GODOT_BIN=/path/to/godot4 scripts/verify_godot_project.sh godot/coin-runner
```

## Publishing examples

Before publishing a generated game example:

- remove editor caches (`.godot/`)
- remove local binaries (`tools/`)
- remove generated builds (`dist/`, `exports/web/`)
- keep only source files, small sample assets, and reproducible scripts
