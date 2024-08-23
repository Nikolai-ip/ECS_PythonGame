from component import Component
from components.transform import Transform
from serviceLocator import ServiceLocator


class Player(Component):

    def __init__(self, health, gameObject=None) -> None:
        super().__init__(gameObject)
        self.origin_health = health
        self.helath = health
    
    def take_damage(self, damage):
        if (self.helath-damage) <= 0:
            self.Die()

    def die(self):
        tr: Transform = self.gameObject.get_component(Transform)
        self.helath = self.origin_health
