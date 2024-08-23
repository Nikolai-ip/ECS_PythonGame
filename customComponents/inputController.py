from component import Component
from Observer.event import Event
from vector2 import Vector2

class InputController(Component):

    def __init__(self, keyboard, gameObject=None) -> None:
        super().__init__(gameObject)
        self.keyboard = keyboard
        self.keyboardButtonPressed = Event()

    def update(self):
        self.handleInput()

    def handleInput(self):
        moveInput = Vector2.zero()
        if self.keyboard.A:
            moveInput += Vector2.left()
        if self.keyboard.D:
            moveInput += Vector2.right()
        if self.keyboard.W: 
            moveInput += Vector2.up()
        if self.keyboard.S: 
            moveInput += Vector2.down()

        self.keyboardButtonPressed.notify(moveInput)

            
