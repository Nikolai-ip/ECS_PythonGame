from customComponents.enemyAI.states.moveToPlayer import MoveToPlayer
from customComponents.enemyAI.states.patrolling import Patrolling
from customComponents.enemyAI.states.states import States
from sceneManager import SceneManager
from stateMachine.stateMachine import StateMachine
from customComponents.enemyAI.enemyMoveController import EnemyMoveController

class EnemyStateMachine(StateMachine):
    
    def __init__(self, gameObject=None) -> None:
        super().__init__(gameObject)
        self.player = SceneManager.get_gameObject('fox')
        move_controller = gameObject.get_component(EnemyMoveController)
        self.states_map[States.PATROLLING] = Patrolling(move_controller,self)
        self.states_map[States.MOVE_TO_PLAYER] = MoveToPlayer(move_controller,self)
        self.current_state = self.states_map[States.PATROLLING]
        self.current_state.enter()

