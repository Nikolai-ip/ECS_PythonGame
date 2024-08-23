from component import Component
from stateMachine.state import State


class StateMachine(Component):

    def __init__(self, gameObject=None):
        super().__init__(gameObject)
        self.states_map = {}
        self.current_state :State = None
    
    def update(self):
        if self.current_state != None:
            self.current_state.update()

    def change_state(self, state_type):
        self.current_state.exit()
        self.current_state = self.states_map[state_type]
        self.current_state.enter()
