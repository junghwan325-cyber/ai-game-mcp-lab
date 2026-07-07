extends CharacterBody3D

signal collected_coin
signal touched_hazard

@export var speed: float = 6.0
@export var jump_velocity: float = 5.0

var gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity")

func _physics_process(delta: float) -> void:
    if not is_on_floor():
        velocity.y -= gravity * delta
    elif Input.is_action_just_pressed("jump"):
        velocity.y = jump_velocity

    var input_dir := Vector2(
        Input.get_action_strength("move_right") - Input.get_action_strength("move_left"),
        Input.get_action_strength("move_back") - Input.get_action_strength("move_forward")
    )
    var direction := Vector3(input_dir.x, 0.0, input_dir.y).normalized()
    velocity.x = direction.x * speed
    velocity.z = direction.z * speed
    move_and_slide()

func reset_to_start() -> void:
    global_position = Vector3(0, 0.8, -6)
    velocity = Vector3.ZERO
