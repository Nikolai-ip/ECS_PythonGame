from Observer.event import Event
from components.animation import Animation
from components.animator import Animator
from gameObject import GameObject
from vector2 import Vector2


class PlayerAnimator(Animator):

    def __init__(self, on_button_pressed:Event, gameobject: GameObject):
        animations_map = {
            'run': Animation(self.load_sprites('fox/run/export'), frame_duration=5),
            'idle':Animation(self.load_sprites('fox/idle'), frame_duration=5)
        }
        super().__init__(animations_map, gameobject)
        self.play_animation('idle')
        on_button_pressed.subscribe(self.on_button_pressed)

    def on_button_pressed(self, *args, **kwargs):
        moveInput: Vector2 = args[0]
        if moveInput != Vector2.zero():
            self.play_animation('run')
        else:
            self.play_animation('idle')




