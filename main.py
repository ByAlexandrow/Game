import random

from functions.health import hero_health
from functions.armor import hero_armor
from functions.attack import hero_physic_attack, reduce_physic_attack, hero_magic_attack, reduce_magic_attack, attack


name = str(input('Введите имя: \n'))
health = int(input('Введите уровень здоровья: \n'))
armor = int(input('Введите стойкость брони: \n'))
physic_attack = int(input('Введите физический урон: \n'))
magic_attack = int(input('Введите магический урон: \n'))


def choose_class(name, health, armor, physic_attack, magic_attack):
    while True:
        print('Выберите класс героя:')
        print('1 - Маг (увеличенный магический урон)')
        print('2 - Воин (увеличенный физический урон)')

        choice = input('Ваш выбор: ')
        choice = choice.lower()

        if choice == '1' or choice == 'маг':
            return Magic(name, health, armor, physic_attack, magic_attack)
        elif choice == '2' or choice == 'воин':
            return Warrior(name, health, armor, physic_attack, magic_attack)
        else:
            print('Вы выбрали несуществующего героя. Рекомендуем выбрать Мага или Воина!')


class Hero:
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.physic_attack = physic_attack
        self.magic_attack = magic_attack
    

    def info(self):
        print(f'\nName - HP - Armor - PhAttack - MgAttack')
        print(f'{self.name} - {self.health} - {self.armor} - {self.physic_attack} - {self.magic_attack}\n')


class Magic(Hero):
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        super().__init__(name, health, armor, physic_attack, magic_attack)
        self.magic_attack = magic_attack + random.randint(5, 15)
        self.physic_attack = reduce_physic_attack(physic_attack)
    

    def attack(self, enemy):
        return attack(self, enemy)


class Warrior(Hero):
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        super().__init__(name, health, armor, physic_attack, magic_attack)
        self.physic_attack = physic_attack + random.randint(5, 15)
        self.magic_attack = reduce_magic_attack(magic_attack)
    

    def attack(self, enemy):
        return attack(self, enemy)


hero_1 = choose_class(name, hero_health(health), hero_armor(armor), hero_physic_attack(physic_attack), hero_magic_attack(magic_attack))
hero_1.info()

hero_1.attack()

while True:
    if choose_class.attack(choose_class): break
    input('Нажмиите любую клавишу для продолжения')
