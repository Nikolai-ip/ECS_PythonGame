from pgzero.actor import Actor
from components.scene import Scene
from components.spriteRenderer import SpriteRender
from components.transform import Transform
from customComponents.inputController import InputController
from customComponents.player import Player
from customComponents.playerAnimator import PlayerAnimator
from customComponents.playerMoveController import PlayerMoveController
from customComponents.restartController import RestartController
from gameObject import GameObject
from serviceLocator import ServiceLocator
from vector2 import Vector2

class PlayerFactory:

    def instantiate_player(self):
        foxActor = Actor('fox/fox')
        fox = GameObject('fox', foxActor)
        windowSize:Vector2 = ServiceLocator.get('windowSize')
        inputController = InputController(ServiceLocator.get('keyboard'))
        fox.add_component(inputController)
        playerMoveController = PlayerMoveController(inputController.keyboardButtonPressed,fox)
        fox.add_component(playerMoveController)
        tr = Transform(foxActor,fox)
        tr.scale_actor(2)
        tr.position = windowSize/2
        fox.add_component(tr).add_component(SpriteRender(foxActor,fox))
        fox.add_component(PlayerAnimator(inputController.keyboardButtonPressed, fox))
        fox.add_component(Player(1,fox))
        fox.add_component(RestartController(fox))

        return fox