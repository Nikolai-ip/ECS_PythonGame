
from component import Component
from components.transform import Transform


class RestartController(Component):

    def __init__(self, gameObject=None) -> None:
        super().__init__(gameObject)
        self.tr:Transform = gameObject.get_component(Transform)
        self.origin_pos = self.tr.position

    def restart(self):
        self.tr.position = self.origin_pos