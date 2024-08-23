from components.animation import Animation
from components.animator import Animator
from gameObject import GameObject

class EnemyAnimator(Animator):

    def __init__(self, gameobject: GameObject):
        animations_map = {
            'idle':Animation(self.load_sprites('enemy'), frame_duration=7)
        }
        super().__init__(animations_map, gameobject)
        self.play_animation('idle')




