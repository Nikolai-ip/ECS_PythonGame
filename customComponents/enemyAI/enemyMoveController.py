from component import Component
from components.transform import Transform
from vector2 import Vector2


class EnemyMoveController(Component):

    def __init__(self, speed, gameObject=None) -> None:
        super().__init__(gameObject)
        self.speed = speed
        self.tr :Transform = gameObject.get_component(Transform)
    
    def move(self, target:Vector2):
        dir = target - self.tr.position
        move =  dir.normalize() * self.speed
        self.tr.position += move