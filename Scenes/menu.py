from Observer.event import Event
from Scenes.gameScene import GameScene
from components.scene import Scene
from sceneManager import SceneManager
from pgzero.actor import Actor

from serviceLocator import ServiceLocator

class Menu(Scene):
    def __init__(self, mouse_button_pressed:Event):
        super().__init__()
        SceneManager.register_scene(Menu,self)
        window_size = ServiceLocator.get('windowSize')
        self.play_button = Actor('ui/play_button', (window_size.x // 2, window_size.y // 2 - 50))
        self.quit_button = Actor('ui/exit_button', (window_size.x // 2, window_size.y // 2 + 150))
        mouse_button_pressed.subscribe(self.on_mouse_button_pressed)


    def draw(self):
        self.play_button.draw()
        self.quit_button.draw()

    def on_mouse_button_pressed(self, *args, **kwargs):
        mouse_pos = args[0]
        if self.play_button.collidepoint(mouse_pos):
            SceneManager.change_scene(GameScene)
        if self.quit_button.collidepoint(mouse_pos):
            quit()
