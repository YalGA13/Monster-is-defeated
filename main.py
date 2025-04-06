from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

# Класс Fighter из исходных данных
class Fighter:
    def __init__(self):
        self._weapon = None  # текущее оружие бойца

    # Шаг 3: Метод для смены оружия
    def change_weapon(self, weapon: Weapon):
        self._weapon = weapon

    def attack(self):
        if not self._weapon:
            raise ValueError("Боец без оружия!")
        return self._weapon.attack()

# Класс Monster из исходных данных
class Monster:
    pass

# Шаг 4: Реализация боя
def battle_demo(fighter: Fighter, monster: Monster):
    # В этом примере монстр всегда побеждается одной атакой
    print(f"Боец выбирает {fighter._weapon.__class__.__name__.lower()}.")
    print(f"Боец {fighter.attack()}.")
    print("Монстр побежден!\n")

# Демонстрация работы программы
if __name__ == "__main__":
    fighter = Fighter()
    monster = Monster()

    # Бой с мечом
    fighter.change_weapon(Sword())
    battle_demo(fighter, monster)

    # Бой с луком
    fighter.change_weapon(Bow())
    battle_demo(fighter, monster)