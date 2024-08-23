
import pgzrun
from Observer.event import Event
from Scenes.gameScene import GameScene
from Scenes.menu import Menu
from my_time import Time
from sceneManager import SceneManager
from serviceLocator import ServiceLocator
import os

from vector2 import Vector2

TITLE = "TEST TASK"
WIDTH = 1200
HEIGHT = 800
os.environ['SDL_VIDEO_CENTERED'] = '1'
music.play('background')
music.set_volume(0.2)
serviceLocator = ServiceLocator()
serviceLocator.register(Vector2(WIDTH,HEIGHT),'windowSize')
serviceLocator.register(keyboard,'keyboard')
mouse_button_pressed=Event()
game = GameScene()
menu = Menu(mouse_button_pressed)
SceneManager.change_scene(Menu)

def draw():
    screen.fill((0,0,0))
    SceneManager.current_scene.draw()

def update():
    SceneManager.current_scene.update()
    Time.update()

def on_mouse_down(button, pos):
    if button == mouse.LEFT:
        mouse_button_pressed.notify(pos)
pgzrun.go()
