from pgzero.actor import Actor
from components.spriteRenderer import SpriteRender
from components.transform import Transform
from customComponents.enemy import Enemy
from customComponents.enemyAI.enemyMoveController import EnemyMoveController
from customComponents.enemyAI.enemyStateMachine import EnemyStateMachine
from customComponents.enemyAnimator import EnemyAnimator
from customComponents.restartController import RestartController
from gameObject import GameObject
from serviceLocator import ServiceLocator
from vector2 import Vector2

class EnemyFactory:
    def instantiate_enemies(self):
        enemies = []
        windowSize:Vector2 = ServiceLocator.get('windowSize')
        enemies.append(self.instantiate_enemy(windowSize/1.5))
        enemies.append(self.instantiate_enemy(windowSize/3.5))
        return enemies


    def instantiate_enemy(self,pos):
        enemyActor = Actor('enemy/sprite-0001')
        enemy = GameObject('enemy', enemyActor)
        tr = Transform(enemyActor,enemy)

        tr.position = pos
        enemy.add_component(tr).add_component(SpriteRender(enemyActor,enemy))
        enemy.add_component(EnemyMoveController(2,enemy))
        enemy.add_component(EnemyStateMachine(enemy))
        enemy.add_component(EnemyAnimator(enemy))
        enemy.add_component(Enemy(enemy))
        enemy.add_component(RestartController(enemy))
        return enemy