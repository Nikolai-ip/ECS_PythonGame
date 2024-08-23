from components.scene import Scene


class SceneManager:
    scenes = {}
    current_scene: Scene = None

    @staticmethod
    def register_scene(type, scene):
        SceneManager.scenes[type] = scene
        if SceneManager.current_scene == None:
            SceneManager.current_scene = scene

    @staticmethod
    def change_scene(type):
        SceneManager.current_scene = SceneManager.scenes[type]

    @staticmethod
    def get_gameObject(name):
        for gameObject in SceneManager.current_scene.gameObjects:
            if gameObject.name == name:
                return gameObject
    
    @staticmethod
    def find_objects_by_type(type):
        find_objects = []
        for gameObject in SceneManager.current_scene.gameObjects:
            if gameObject.get_component(type) != None:
                find_objects.append(gameObject.get_component(type))
        return find_objects
            
    @staticmethod
    def draw():
        SceneManager.current_scene.draw()

    @staticmethod
    def update():
        SceneManager.current_scene.update()