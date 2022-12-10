import random


class Mob:
    def __init__(self):
        self.healgh = 0
        self.damage = 0

    def attack(self, enemy):
        a = random.randint(1, 3)
        if self.real_damage >= enemy.real_armor*2:
            if a == 1:
                enemy.healgh -= round(self.real_damage / 2) - enemy.real_armor
                return int(round(self.real_damage / 2)) - enemy.real_armor
            elif a == 2:
                enemy.healgh -= self.real_damage - enemy.real_armor
                return self.real_damage - enemy.real_armor
            else:
                enemy.healgh -= self.real_damage * 2 - enemy.real_armor
                return self.real_damage * 2 - enemy.real_armor
        elif a == 1 and self.real_damage >= enemy.real_armor:
            return 0
        elif self.real_damage >= enemy.real_armor:
            if a == 2:
                enemy.healgh -= self.real_damage - enemy.real_armor
                return self.real_damage - enemy.real_armor
            else:
                enemy.healgh -= self.real_damage * 2 - enemy.real_armor
        else:
            return 0
