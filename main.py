import random

from functions.health import hero_health
from functions.armor import hero_armor
from functions.attack import hero_physic_attack, reduce_physic_attack, hero_magic_attack, reduce_magic_attack


name = str(input('Введите имя: \n'))
health = int(input('Введите уровень здоровья: \n'))
armor = int(input('Введите стойкость брони: \n'))
physic_attack = int(input('Введите физический урон: \n'))
magic_attack = int(input('Введите магический урон: \n'))


class Hero:
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.physic_attack = physic_attack
        self.magic_attack = magic_attack
    

    def info(self):
        self.health = hero_health(self.health)
        self.armor = hero_armor(self.armor)
        self.physic_attack = hero_physic_attack(self.physic_attack)
        self.magic_attack = hero_magic_attack(self.magic_attack)
        print(f'\nName - HP - Armor - Ph-Attack - MgAttack')
        print(f'{self.name} - {self.health} - {self.armor} - {self.physic_attack} - {self.magic_attack}\n')


class Magic(Hero):
    magic_attack = magic_attack + random.randint(5, 15)
    physic_attack = reduce_physic_attack(physic_attack)


class Warrior(Hero):
    physic_attack = physic_attack + random.randint(5, 15)
    magic_attack = reduce_magic_attack(magic_attack)


hero_1 = Hero(name, health, armor, physic_attack, magic_attack)
hero_1.info()
