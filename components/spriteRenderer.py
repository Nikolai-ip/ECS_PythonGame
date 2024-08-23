from component import Component

class SpriteRender(Component):
    def __init__(self, actor,gameobject):
        super().__init__(gameobject)
        self.actor = actor

    def draw(self):
        self.actor.draw()
    
    def set_sprite(self, sprite):
        self.actor.image = sprite
        