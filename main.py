user_choice = str(input('\n'))
name = str(input('Введите имя: \n'))
health = int(input('Введите уровень здоровья: \n'))
armor = int(input('Введите стойкость брони: \n'))
attack_force = int(input('Введите физический урон: \n'))


def choice(user_choice, a, b, c):
    """Функция корректирует значение здоровья героя."""
    if user_choice == a:
        result = a
    elif result == b:
        result = b
    else:
       result = c
    
    return result


def hero_health(health):
    """Функция корректирует значение здоровья героя."""
    if health >= 100:
        health = 100
    elif 100 < health or health > 50:
        health = 75
    else:
       health = 50
    
    return health


def hero_armor(armor):
    """Функция корректирует значение брони героя."""
    if armor >= 150:
        armor = 150
    elif 150 < armor or armor > 75:
        armor = 100
    else:
        armor = 50
    
    return armor


def hero_attack_force(attack_force):
    """Функция корректирует значение силы атаки героя."""
    if attack_force >= 50:
        attack_force = 50
    elif 30 < attack_force or attack_force < 50:
        attack_force = 30
    else:
        attack_force = 10
    
    return attack_force


class Hero:
    def __init__(self, result, name, health, armor, attack_force):
        self.result = result
        self.name = name # строка
        self.health = health # число
        self.armor = armor # число
        self.attack_force = attack_force # число
    

    def info(self):
        self.result = choice(self.result)
        self.health = hero_health(self.health)
        self.armor = hero_armor(self.armor)
        self.attack_force = hero_attack_force(self.attack_force)
        print(f'\nClass - Name - HP - Armor - Attack')
        print(f'{self.result} - {self.name} - {self.health} - {self.armor} - {self.attack_force}\n')


class Magic(Hero):
    attack_magic = int(input('Введите магический урон: \n'))
    
    def hero_attack_magic(attack_magic):
        """Функция корректирует значение силы атаки героя."""
        if attack_magic >= 65:
            attack_magic = 65
        elif 45 < attack_magic or attack_magic < 65:
            attack_magic = 45
        else:
            attack_magic = 25
    
        return attack_magic
    


class Warrior:
    ...


hero_1 = Hero(user_choice, name, health, armor, attack_force)
hero_1.info()
