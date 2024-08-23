import random
from customComponents.enemyAI.states.states import States
from stateMachine.state import State
from components.transform import Transform
from customComponents.enemyAI.enemyMoveController import EnemyMoveController
from stateMachine.stateMachine import StateMachine
from vector2 import Vector2


class Patrolling(State):

    def __init__(self, move_controller:EnemyMoveController, state_machine:StateMachine) -> None:
        self.state_machine = state_machine
        self.move_controller = move_controller
        self.player_tr:Transform = state_machine.player.get_component(Transform)
        self.tr:Transform = state_machine.gameObject.get_component(Transform)
        self.dist_to_move = 250
        self.move_target = self.tr.position
        self.patrol_raduis = 100
        self.pull_koef = 3
    

    def update(self):
        distnace = Vector2.distance(self.move_target,self.tr.position)
        if distnace<2:
            rand_vector = Vector2(random.randint(-self.patrol_raduis,self.patrol_raduis),random.randint(-self.patrol_raduis,self.patrol_raduis))
            rand_vector += (self.player_tr.position - self.tr.position).normalize() * 3
            self.move_target = self.tr.position+rand_vector
        self.move_controller.move(self.move_target)
        self.check_transition()

    def check_transition(self):
        if Vector2.distance(self.tr.position, self.player_tr.position)<self.dist_to_move:
            self.state_machine.change_state(States.MOVE_TO_PLAYER)
