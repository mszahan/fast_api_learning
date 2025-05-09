from Enemy import *
from Zombie import Zombie
from Ogre import Ogre

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

# this falls into the polymorphism of object
def battle(e: Enemy):
    e.talk()
    e.attack()


battle(zombie)
battle(ogre)

# print(zombie.get_type_of_enemy())
# zombie.spread_disease()




# roman = Enemy('roman', 10, 1)
# enemy.type_of_enemy = 'Roman'

# roman.talk()
# print(roman.get_type_of_enemy())
# print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do attack {enemy.attack_damage}')