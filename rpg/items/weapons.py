import random


class Weapon:
    def __init__(self):
        self.base_damage = 0
        self.modifier = 0

    @property
    def real_damage(self):
        return self.base_damage + self.modifier

    def __str__(self):
        return "None"


class ShortSword(Weapon):
    def __init__(self):
        super().__init__()
        self.cost = 200
        self.base_damage = 5
        self.modifier = random.randint(-self.base_damage, self.base_damage)

    def __str__(self):
        return f"Short sword \n deals: {self.real_damage} dmg "
