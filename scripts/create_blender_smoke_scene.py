#!/usr/bin/env python3
"""Create a small low-poly Blender scene and export it as GLB.

Run with:
  blender --background --python scripts/create_blender_smoke_scene.py
"""

from pathlib import Path

import bpy

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build" / "blender" / "smoke_scene.glb"
OUT.parent.mkdir(parents=True, exist_ok=True)

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

# Floor
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.05))
floor = bpy.context.object
floor.name = "floor_test"
floor.dimensions = (6, 6, 0.1)
mat_floor = bpy.data.materials.new("mat_floor_green")
mat_floor.diffuse_color = (0.2, 0.6, 0.25, 1)
floor.data.materials.append(mat_floor)

# Player marker
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.55))
player = bpy.context.object
player.name = "player_test_cube"
mat_player = bpy.data.materials.new("mat_player_blue")
mat_player.diffuse_color = (0.1, 0.35, 1.0, 1)
player.data.materials.append(mat_player)

# Obstacles
for index, x in enumerate([-2, 2], start=1):
    bpy.ops.mesh.primitive_cube_add(size=0.8, location=(x, 1.5, 0.4))
    obstacle = bpy.context.object
    obstacle.name = f"obstacle_test_{index}"
    mat = bpy.data.materials.new(f"mat_obstacle_{index}")
    mat.diffuse_color = (0.9, 0.25, 0.15, 1)
    obstacle.data.materials.append(mat)

# Camera/light
bpy.ops.object.light_add(type="SUN", location=(2, -3, 5))
bpy.context.object.name = "sun_test"
bpy.ops.object.camera_add(location=(4, -6, 4), rotation=(1.1, 0, 0.62))
bpy.context.scene.camera = bpy.context.object

bpy.ops.export_scene.gltf(filepath=str(OUT), export_format="GLB")
print(f"WROTE {OUT}")
