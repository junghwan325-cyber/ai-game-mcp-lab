# Architecture

AI Game MCP Lab keeps the reusable pieces of an AI-assisted game prototyping workflow in a small public repository.

## Flow

```text
prompt template
  -> AI agent
  -> Blender Python or Blender MCP
  -> GLB/GLTF asset
  -> Godot 4 project
  -> headless load/export verification
```

## Layers

| Layer | Role | Example output |
| --- | --- | --- |
| Prompt | Specify style, asset requirements, safety constraints | `prompts/game_asset_and_godot.md` |
| Blender | Generate or edit low-poly 3D assets | `.glb`, `.blend` in `build/` |
| Godot | Compose scenes, gameplay logic, UI, exports | `project.godot`, `.tscn`, `.gd` |
| Verification | Check that assets/projects load in headless mode | success markers in scripts |

## Why headless verification matters

AI-generated assets and scenes can look plausible but fail to load because of missing resources, invalid imports, or editor-only caches. Headless checks make the workflow reproducible on a server or CI runner.

## Extending the lab

- Add new prompt templates under `prompts/`.
- Add deterministic Blender scripts under `scripts/`.
- Keep generated binary artifacts under `build/` or `exports/`.
- Keep local third-party MCP checkouts under `mcp/`, which is gitignored.
