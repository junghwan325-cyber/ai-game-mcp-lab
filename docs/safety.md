# MCP safety

Blender MCP and similar creative tool servers often expose commands that can execute Python or manipulate files. Treat them like local developer shells.

## Safe defaults

- Bind MCP servers to `127.0.0.1` only.
- Do not expose Blender/Godot MCP ports to the public internet.
- Run experiments inside a bounded working directory.
- Keep generated assets in gitignored directories such as `build/` or `exports/`.
- Review generated Python/GDScript before using it in a real project.

## Never include in prompts or repos

- `.env` contents
- API keys
- OAuth tokens
- cookies
- private keys
- paid or non-redistributable assets
- personal photos or private user data

## Generated text in images

For games that render UI separately, keep generated 3D assets text-free: no labels, logos, fake letters, watermarks, or readable signs unless the asset explicitly needs them and licensing is clear.
