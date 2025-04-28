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
