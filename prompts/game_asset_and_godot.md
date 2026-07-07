# Game asset and Godot prompt templates

## Blender / Blender MCP asset prompt

```text
Create low-poly game assets for a mobile/web-friendly Godot prototype.

Requirements:
- Style: bright, readable, low-poly.
- Output: GLB or GLTF.
- Keep polygon count low.
- Use English snake_case object names so Godot imports are easy to inspect.
- Do not include text, logos, watermarks, labels, or fake writing.
- Add custom properties when useful, e.g. node_type, collectible, hazard, spawn, goal.
- Export into the project build directory, not a private absolute server path.

Assets:
- <describe objects>
```

## Godot scene prompt

```text
Create a Godot 4 mini-game scene using imported GLB assets.

Requirements:
- Player movement: WASD/arrow keys and Space jump.
- Collectibles with score UI.
- Hazards that reset the player.
- Goal area that checks completion.
- Web/HTML5 friendly rendering settings.
- Keep secrets out of code and logs.
- Do not read or print .env, token files, cookies, or private keys.
```

## Agent handoff checklist

- What project path should be used?
- Which generated assets are expected?
- Which files may be modified?
- Which verification command proves success?
- What should be excluded from git?
