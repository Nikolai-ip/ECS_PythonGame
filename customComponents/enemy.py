from component import Component
from pgzero.actor import Actor
from customComponents.player import Player
from customComponents.restartController import RestartController
from sceneManager import SceneManager


class Enemy(Component):

    def __init__(self, gameObject=None) -> None:
        super().__init__(gameObject)
        self.player: Player = SceneManager.get_gameObject('fox').get_component(Player)
        self.actor:Actor = gameObject.get_actor()

    def update(self):
        if self.actor.colliderect(self.player.gameObject.get_actor()):
            self.player.die()
            for restartable in SceneManager.find_objects_by_type(RestartController):
                restartable.restart()
