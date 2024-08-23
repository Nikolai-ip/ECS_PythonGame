from components.spriteRenderer import SpriteRender
from components.transform import Transform


class GameObject:
    def __init__(self, name,actor):
        self.name = name
        self.actor = actor
        self.components = {}
        

    def add_component(self, component):
        self.components[type(component)] = component
        return self

    def get_component(self, component_type):
        return self.components.get(component_type)

    def update(self):
        for component in self.components.values():
            component.update()

    def draw(self):
        for component in self.components.values():
            component.draw()
    
    def get_actor(self):
        return self.actor