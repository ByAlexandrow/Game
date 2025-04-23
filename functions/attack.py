import random

from ..main import Magic, Warrior


def hero_physic_attack(physic_attack):
    """Функция корректирует значение физической атаки героя."""
    if physic_attack >= 50:
        physic_attack = 50
    elif 30 < physic_attack or physic_attack < 50:
        physic_attack = 30
    else:
        physic_attack = 10
    
    return physic_attack


def reduce_physic_attack(physic_attack):
    """Функция уменьшает значение физической атаки героя."""
    if physic_attack == 50:
        physic_attack = 25
    elif physic_attack == 30:
        physic_attack = 15
    else:
        physic_attack = 5
    
    return physic_attack


def hero_magic_attack(magic_attack):
    """Функция корректирует значение магической атаки героя."""
    if magic_attack >= 50:
        magic_attack = 50
    elif 30 < magic_attack or magic_attack < 50:
        magic_attack = 30
    else:
        magic_attack = 10
    
    return magic_attack


def reduce_magic_attack(magic_attack):
    """Функция уменьшает значение магической атаки героя."""
    if magic_attack == 50:
        magic_attack = 25
    elif magic_attack == 30:
        magic_attack = 15
    else:
        magic_attack = 5
    
    return magic_attack


def attack(self, enemy):
    if isinstance(self, Magic):
        if enemy.armor > 0:
            crush_armor = min(self.magic_attack, enemy.armor)
            enemy.armor -= crush_armor
            print(f'Вы теряете {crush_armor} брони')
        else:
            enemy.health -= self.magic_attack
            print(f'Вы теряете {self.magic_attack} XP')

    elif isinstance(self, Warrior):
        if enemy.armor > 0:
            ...
        else:
            enemy.health -= self.physic_attack

    else:
        print('Вы одержали победу!')
