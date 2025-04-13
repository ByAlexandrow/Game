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
