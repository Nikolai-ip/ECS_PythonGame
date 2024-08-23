from component import Component
from Observer.event import Event
from gameObject import GameObject
from components.transform import Transform 
from my_time import Time
from vector2 import Vector2

class PlayerMoveController(Component):
    
    def __init__(self,  buttonPressed:Event, gameObject:GameObject = None) -> None:
        self.gameObject = gameObject
        buttonPressed.subscribe(self.on_button_pressed)
    
    def on_button_pressed(self, *args, **kwargs):
        tr: Transform = self.gameObject.get_component((Transform))
        moveInput: Vector2 = args[0]
        
        tr.position = tr.position + (moveInput.normalize() * 250 * Time.delta_time)
