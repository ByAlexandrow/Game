import random

from functions.health import hero_health
from functions.armor import hero_armor
from functions.attack import hero_physic_attack, reduce_physic_attack, hero_magic_attack, reduce_magic_attack


name = str(input('Введите имя: \n'))
health = int(input('Введите уровень здоровья: \n'))
armor = int(input('Введите стойкость брони: \n'))
physic_attack = int(input('Введите физический урон: \n'))
magic_attack = int(input('Введите магический урон: \n'))


def choose_class(name, health, armor, physic_attack, magic_attack):
    """Функция выбора класса."""
    while True:
        print('\nВыберите класс героя:')
        print('1 - Маг (увеличенный магический урон)')
        print('2 - Воин (увеличенный физический урон)')

        choice = input('\nВаш выбор: ')
        choice = choice.lower()

        if choice == '1' or choice == 'маг':
            return Magic(name, health, armor, physic_attack, magic_attack)
        elif choice == '2' or choice == 'воин':
            return Warrior(name, health, armor, physic_attack, magic_attack)
        else:
            print('Вы выбрали несуществующего героя. Рекомендуем выбрать Мага или Воина!')


def choose_difficulty():
    """Функция выбора уровня сложности."""
    while True:
        print('\nВыберите уровень сложности:')
        print('1 - Легкий')
        print('2 - Средний')
        print('3 - Сложный')
        
        choice = input('\nВаш выбор: ')
        choice = choice.lower()
        
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print('Некорректный ввод! Пожалуйста, выберите 1, 2 или 3')


def create_enemy(difficulty, hero_class):
    """Функция создания противника в зависимости от уровня сложности."""
    if difficulty == 1:
        health = random.randint(40, 60)
        armor = random.randint(30, 50)
        physic_attack = random.randint(10, 20)
        magic_attack = random.randint(10, 20)
    elif difficulty == 2:
        health = random.randint(60, 80)
        armor = random.randint(50, 70)
        physic_attack = random.randint(20, 30)
        magic_attack = random.randint(20, 30)
    else:
        health = random.randint(80, 100)
        armor = random.randint(70, 90)
        physic_attack = random.randint(30, 40)
        magic_attack = random.randint(30, 40)
    
    if isinstance(hero_class, Magic):
        physic_attack += random.randint(5, 15)
        magic_attack = reduce_magic_attack(magic_attack)
    else:
        magic_attack += random.randint(5, 15)
        physic_attack = reduce_physic_attack(physic_attack)
    
    enemy_class = random.choice(['Magic', 'Warrior'])
    name = random.choice(['Гоблин', 'Орк', 'Тролль', 'Демон', 'Скелет', 'Зомби'])
    
    if enemy_class == 'Magic':
        return Magic(name, health, armor, physic_attack, magic_attack)
    else:
        return Warrior(name, health, armor, physic_attack, magic_attack)


def battle(player, enemy):
    """Функция атаки."""
    print(f"\nБой начинается!\n{player.name} VS {enemy.name}\n")
    
    round_num = 1
    while player.health > 0 and enemy.health > 0:
        print(f"=== Раунд {round_num} ===")
        
        player_attack_type = input("Выберите тип атаки (1 - физическая, 2 - магическая): ")
        if player_attack_type == '1':
            damage = player.physic_attack - (enemy.armor // 10)
            damage = max(1, damage)
            enemy.health -= damage
            print(f"{player.name} наносит {damage} физического урона!\nУ {enemy.name} осталось {max(0, enemy.health)} здоровья.")
        else:
            damage = player.magic_attack - (enemy.armor // 20)
            damage = max(1, damage)
            enemy.health -= damage
            print(f"{player.name} наносит {damage} магического урона!\nУ {enemy.name} осталось {max(0, enemy.health)} здоровья.")
        
        if enemy.health <= 0:
            break

        if random.random() < 0.5:
            damage = enemy.physic_attack - (player.armor // 10)
            damage = max(1, damage)
            player.health -= damage
            print(f"{enemy.name} наносит {damage} физического урона! У {player.name} осталось {max(0, player.health)} здоровья.")
        else:
            damage = enemy.magic_attack - (player.armor // 20)
            damage = max(1, damage)
            player.health -= damage
            print(f"{enemy.name} наносит {damage} магического урона! У {player.name} осталось {max(0, player.health)} здоровья.")
        
        round_num += 1
        print()
    
    if player.health > 0:
        print(f"\nWINNER!\n{player.name} победил!")
    else:
        print(f"\nLOSER!\n{enemy.name} оказался сильнее.")


class Hero:
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.physic_attack = physic_attack
        self.magic_attack = magic_attack
    

    def info(self):
        print(f'Name - HP - Armor - PhAttack - MgAttack')
        print(f'{self.name} - {self.health} - {self.armor} - {self.physic_attack} - {self.magic_attack}\n')


class Magic(Hero):
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        super().__init__(name, health, armor, physic_attack, magic_attack)
        self.magic_attack = magic_attack + random.randint(5, 15)
        self.physic_attack = reduce_physic_attack(physic_attack)


class Warrior(Hero):
    def __init__(self, name, health, armor, physic_attack, magic_attack):
        super().__init__(name, health, armor, physic_attack, magic_attack)
        self.physic_attack = physic_attack + random.randint(5, 15)
        self.magic_attack = reduce_magic_attack(magic_attack)


hero = choose_class(name, hero_health(health), hero_armor(armor), hero_physic_attack(physic_attack), hero_magic_attack(magic_attack))
hero.info()

difficulty = choose_difficulty()

enemy = create_enemy(difficulty, hero)
print("\nВаш противник:")
enemy.info()

battle(hero, enemy)
