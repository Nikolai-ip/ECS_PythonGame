from component import Component
from vector2 import Vector2
import pygame

class Transform(Component):
    def __init__(self,actor,gameobject):
        super().__init__(gameobject)
        self.position = Vector2()
        self.scale = Vector2(1,1)
        self.actor = actor


    def update(self):
        self.actor.x = self.position.x
        self.actor.y = self.position.y

    
    def scale_actor(self, scale_factor):
        original_image = pygame.image.load('images/' + self.actor.image + '.png')
        width = int(original_image.get_width() * scale_factor)
        height = int(original_image.get_height() * scale_factor)
        scaled_image = pygame.transform.scale(original_image, (width, height))
        self.scale = Vector2(width,height)

        self.actor._surf = scaled_image
        self.actor.width, self.actor.height = scaled_image.get_size()
