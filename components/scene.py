from component import Component

class Scene(Component):
    def __init__(self):
        super().__init__()
        self.gameObjects = []

    def initGameObject(self,gameObject):
        self.gameObjects.append(gameObject)

    def update(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    def draw(self):
        for gameObject in self.gameObjects:
            gameObject.draw()