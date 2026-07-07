#!/usr/bin/env python3
"""Create low-poly coin-runner assets directly in Blender.

This is the deterministic, no-MCP version. You can adapt the same scene-building
code for a local Blender MCP `execute_python` call if desired.
"""

from __future__ import annotations

import math
from pathlib import Path

import bpy

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "build" / "coin-runner-assets"
GLB_OUT = OUT_DIR / "coin_runner_assets.glb"
BLEND_OUT = OUT_DIR / "coin_runner_assets.blend"


def make_mat(name: str, color, metallic: float = 0.0, roughness: float = 0.5, emission=None, strength: float = 0.0):
    material = bpy.data.materials.new(name)
    material.use_nodes = True
    bsdf = material.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Metallic"].default_value = metallic
        bsdf.inputs["Roughness"].default_value = roughness
        if emission:
            bsdf.inputs["Emission Color"].default_value = emission
            bsdf.inputs["Emission Strength"].default_value = strength
    else:
        material.diffuse_color = color
    return material


OUT_DIR.mkdir(parents=True, exist_ok=True)
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

mat_floor = make_mat("mat_grass_floor", (0.16, 0.62, 0.25, 1), roughness=0.8)
mat_player = make_mat("mat_player_blue", (0.08, 0.32, 1.0, 1), roughness=0.45)
mat_coin = make_mat(
    "mat_coin_gold",
    (1.0, 0.72, 0.06, 1),
    metallic=0.4,
    roughness=0.25,
    emission=(1.0, 0.52, 0.03, 1),
    strength=0.25,
)
mat_obstacle = make_mat("mat_obstacle_red", (0.92, 0.12, 0.08, 1), roughness=0.6)
mat_goal = make_mat(
    "mat_goal_green_emission",
    (0.1, 1.0, 0.3, 1),
    emission=(0.1, 1.0, 0.3, 1),
    strength=0.6,
)

# Floor
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.05))
floor = bpy.context.object
floor.name = "level_floor"
floor.dimensions = (12, 16, 0.1)
floor.location = (0, 0, -0.05)
floor.data.materials.append(mat_floor)
floor["node_type"] = "StaticBody3D"
floor["collision_shape"] = "box"

# Player marker asset
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -6, 0.5))
player = bpy.context.object
player.name = "player_cube_start"
player.scale = (0.55, 0.55, 0.55)
player.data.materials.append(mat_player)
player["node_type"] = "CharacterBody3D"
player["spawn"] = True

# Coins
for index, (x, y) in enumerate([(-3, -3), (0, -2), (3, -1), (-2, 2), (2, 4)], start=1):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=24,
        radius=0.35,
        depth=0.12,
        location=(x, y, 0.55),
        rotation=(math.pi / 2, 0, 0),
    )
    coin = bpy.context.object
    coin.name = f"coin_{index:02d}"
    coin.data.materials.append(mat_coin)
    coin["node_type"] = "Area3D"
    coin["collectible"] = True

# Obstacles
for index, (x, y, sx, sy) in enumerate(
    [(-1.8, 0.2, 1.6, 0.45), (2.2, 1.8, 0.45, 1.8), (0, 5.5, 3.2, 0.45)],
    start=1,
):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0.45))
    obstacle = bpy.context.object
    obstacle.name = f"obstacle_{index:02d}"
    obstacle.scale = (sx, sy, 0.45)
    obstacle.data.materials.append(mat_obstacle)
    obstacle["node_type"] = "StaticBody3D"
    obstacle["hazard"] = True

# Goal gate
bpy.ops.mesh.primitive_torus_add(
    major_radius=0.8,
    minor_radius=0.08,
    major_segments=32,
    minor_segments=8,
    location=(0, 7, 0.9),
    rotation=(math.pi / 2, 0, 0),
)
goal = bpy.context.object
goal.name = "goal_ring"
goal.data.materials.append(mat_goal)
goal["node_type"] = "Area3D"
goal["goal"] = True

# Lights/camera reference
bpy.ops.object.light_add(type="SUN", location=(0, -2, 8))
sun = bpy.context.object
sun.name = "sun_key_light"
sun.data.energy = 2.5
bpy.ops.object.camera_add(location=(0, -10, 9), rotation=(math.radians(58), 0, 0))
bpy.context.object.name = "camera_reference"
bpy.context.scene.camera = bpy.context.object

bpy.ops.wm.save_as_mainfile(filepath=str(BLEND_OUT))
bpy.ops.export_scene.gltf(filepath=str(GLB_OUT), export_format="GLB", export_cameras=False, export_lights=False)
print({"glb": str(GLB_OUT), "blend": str(BLEND_OUT), "objects": len(bpy.data.objects)})
