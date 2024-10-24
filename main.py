from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack_monster(self, monster):
        if self.weapon:
            print(self.weapon.attack())
            if monster.take_damage():
                print("Монстр побежден!")
            else:
                print("Монстр жив!")
        else:
            print("У бойца нет оружия!")

# Класс Monster
class Monster:
    def __init__(self, health):
        self.health = health

    def take_damage(self):
        damage = random.randint(1, 2)  # Урон от атаки
        self.health -= damage
        return self.health <= 0

# Шаг 4: Реализация боя
def main():
    fighter = Fighter("Герой")
    monster = Monster(3)  # Здоровье монстра

    # Бой с мечом
    fighter.change_weapon(Sword())
    fighter.attack_monster(monster)

    # Если монстр еще жив, сменим оружие на лук
    if monster.health > 0:
        fighter.change_weapon(Bow())
        fighter.attack_monster(monster)

if __name__ == "__main__":
    main()