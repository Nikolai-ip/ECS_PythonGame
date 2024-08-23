from components.transform import Transform
from customComponents.enemyAI.enemyMoveController import EnemyMoveController
from customComponents.enemyAI.states.states import States
from stateMachine.state import State
from stateMachine.stateMachine import StateMachine
from vector2 import Vector2

class MoveToPlayer(State):
    
    def __init__(self, move_controller, state_machine:StateMachine) -> None:
        self.state_machine = state_machine
        self.move_controller:EnemyMoveController = move_controller
        self.player_tr:Transform = state_machine.player.get_component(Transform)
        self.distance_to_patrol = 300
        self.tr:Transform = state_machine.gameObject.get_component(Transform)


    def update(self):
        self.move_controller.move(self.player_tr.position)
        self.check_transition()
    
    def check_transition(self):
        if  Vector2.distance(self.tr.position, self.player_tr.position)>self.distance_to_patrol:
            self.state_machine.change_state(States.PATROLLING)