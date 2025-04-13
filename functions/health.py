def hero_health(health):
    """Функция корректирует значение здоровья героя."""
    if health >= 100:
        health = 100
    elif 100 < health or health > 50:
        health = 75
    else:
       health = 50
    
    return health
