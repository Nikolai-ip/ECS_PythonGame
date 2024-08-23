import os
from component import Component
from components.spriteRenderer import SpriteRender
from gameObject import GameObject

class Animator(Component):
    def __init__(self, animations_map,gameobject:GameObject):
        super().__init__(gameobject)
        self.animations_map = animations_map
        self.current_animation = None
        self.actor = gameobject.get_actor()
        self.sr = gameobject.get_component(SpriteRender)

    def play_animation(self, name):
        if name in self.animations_map:
            self.current_animation = self.animations_map[name]
            sprite = self.current_animation.get_current_sprite()
            self.sr.set_sprite(sprite)

    def update(self):
        if self.current_animation:
            self.current_animation.update()
            self.actor.image = self.current_animation.get_current_sprite()

    def load_sprites(self, folder):
        sprite_files = sorted(os.listdir(f'images/{folder}'))
        sprites = [f'{folder}/{sprite_file[:-4]}' for sprite_file in sprite_files if sprite_file.endswith('.png')]
        return sprites

    def draw(self):
        if self.actor:
            self.actor.draw()
