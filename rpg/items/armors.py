import random


class Armor:
    def __init__(self):
        self.base_armor = 0
        self.modifier = 0

    @property
    def real_armor(self):
        return self.base_armor + self.modifier

    def __str__(self):
        return 'None'


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__()
        self.cost = 500
        self.base_armor = 3
        self.modifier = random.randint(-self.base_armor, self.base_armor)

    def __str__(self):
        return f"Leather armor, \n absorbs {self.real_armor} dmg"
