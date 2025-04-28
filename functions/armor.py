def hero_armor(armor):
    """Функция корректирует значение брони героя."""
    if armor >= 150:
        armor = 150
    elif 75 < armor < 150:
        armor = 100
    else:
        armor = 50
    
    return armor
