# AI Game MCP Lab

A public, secret-free lab for experimenting with AI-assisted game creation using Blender, Godot, and MCP-style workflows.

The repository is extracted from a real self-hosted experiment where AI agents generated low-poly Blender assets, exported GLB files, assembled a Godot 4 mini-game, and verified the project in headless mode. It intentionally excludes local binaries, credentials, generated caches, and private server paths.

## What this is

- A small reproducible lab for AI-assisted game prototyping
- Blender scripts for headless low-poly asset generation
- A Godot 4 sample project (`coin-runner`) with movement, coins, hazards, and a goal
- Verification scripts for Blender and Godot headless workflows
- Prompt templates for using an AI agent with Blender/Godot MCP tools
- Safety notes for running MCP servers locally without exposing arbitrary code execution

## What this is not

- It does not include Blender or Godot binaries
- It does not include private MCP credentials or server tokens
- It does not expose an MCP server to the network
- It is not a production game engine framework

## Architecture

```text
AI agent / Claude / Codex / Hermes
  -> prompt templates
  -> Blender or Blender MCP
  -> GLB/GLTF assets
  -> Godot 4 project
  -> headless load/export checks
```

## Quick start

### 1. Verify repository-only checks

```bash
python3 -m unittest discover -s tests -v
```

### 2. Optional: generate Blender assets

Requires Blender in `PATH`, or set `BLENDER_BIN`.

```bash
scripts/verify_blender_headless.sh
```

This writes sample GLB/Blend artifacts under `build/`, which is gitignored.

### 3. Optional: verify Godot project load

Requires Godot 4 in `PATH`, or set `GODOT_BIN`.

```bash
GODOT_BIN=/path/to/godot4 scripts/verify_godot_project.sh godot/coin-runner
```

Expected success marker:

```text
GODOT_PROJECT_LOAD_OK
```

## Sample project

`godot/coin-runner` is a tiny 3D collection game:

- WASD / arrow keys move
- Space jumps
- 5 coins to collect
- red hazards reset the player
- goal checks whether all coins were collected

The project includes a small GLB sample asset so it can be inspected without regenerating Blender output.

## Repository layout

```text
docs/                     Architecture and MCP safety notes
godot/coin-runner/        Godot 4 sample game
prompts/                  AI agent prompt templates
scripts/                  Blender/Godot verification helpers
samples/assets/           Small checked-in sample GLB assets
src/ai_game_mcp_lab/      Local Python helpers used by tests
tests/                    Secret/path/package checks
```

## MCP safety defaults

Blender MCP and similar tools can execute Python inside Blender. Treat them as local privileged developer tools:

- bind to localhost only
- never expose MCP ports publicly
- never paste `.env`, tokens, cookies, private keys, or OAuth files into prompts
- keep generated assets under `build/`, `exports/`, or another gitignored path
- review generated code before running it in a real game project

See [docs/safety.md](docs/safety.md).

## Claude for OSS context

This repo is a reusable OSS extraction of a self-hosted AI game prototyping workflow: prompt templates, headless Blender/Godot scripts, a sample project, and safety checks that other creators can inspect and adapt.

## License

MIT — see [LICENSE](./LICENSE).
