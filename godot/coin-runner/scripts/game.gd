extends Node3D

@onready var player: CharacterBody3D = $Player
@onready var score_label: Label = $UI/ScoreLabel
@onready var message_label: Label = $UI/MessageLabel

var score := 0
var total_coins := 5

func _ready() -> void:
    _update_score()
    for coin in get_tree().get_nodes_in_group("coins"):
        coin.body_entered.connect(_on_coin_body_entered.bind(coin))
    for hazard in get_tree().get_nodes_in_group("hazards"):
        hazard.body_entered.connect(_on_hazard_body_entered)
    $Goal.body_entered.connect(_on_goal_body_entered)

func _on_coin_body_entered(body: Node3D, coin: Area3D) -> void:
    if body != player or not coin.visible:
        return
    coin.visible = false
    coin.set_deferred("monitoring", false)
    score += 1
    message_label.text = "코인 획득!"
    _update_score()

func _on_hazard_body_entered(body: Node3D) -> void:
    if body != player:
        return
    message_label.text = "장애물! 시작점으로 돌아가요."
    player.reset_to_start()

func _on_goal_body_entered(body: Node3D) -> void:
    if body != player:
        return
    if score >= total_coins:
        message_label.text = "성공! 모든 코인을 모았어요."
    else:
        message_label.text = "코인을 모두 모아야 해요."

func _update_score() -> void:
    score_label.text = "Score: %d / %d" % [score, total_coins]
