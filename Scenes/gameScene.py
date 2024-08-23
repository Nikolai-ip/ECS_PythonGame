from components.scene import Scene
from customComponents.inputController import InputController
from customComponents.playerAnimator import PlayerAnimator
from customComponents.playerMoveController import PlayerMoveController
from factories.enemyFactory import EnemyFactory
from factories.playerFactory import PlayerFactory
from sceneManager import SceneManager
from serviceLocator import ServiceLocator

class GameScene(Scene):

    def __init__(self):
        super().__init__()
        SceneManager.register_scene(GameScene,self)
        self.init_player()
        self.init_enemy()
    
    def init_player(self):
        playerFactory = PlayerFactory()
        player = playerFactory.instantiate_player()
        self.initGameObject(player)
    
    def init_enemy(self):
        enemy_factory = EnemyFactory()
        for enemy in enemy_factory.instantiate_enemies():
            self.initGameObject(enemy)
        