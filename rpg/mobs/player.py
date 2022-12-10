from rpg.mobs import mob
from rpg.items import armors, weapons


class Player(mob.Mob):

    def __init__(self):
        super().__init__()
        self.armor = armors.Armor()
        self.base_damage = 10
        self.weapon = weapons.Weapon()
        self.Max_healgh = 100
        self.healgh = 100
        self.coins = 0
        self.inventory = []
        self.max_slots = 5

    @property
    def real_damage(self):
        return self.weapon.real_damage + self.base_damage

    @property
    def real_armor(self):
        return self.armor.real_armor

    def take_on_weapon(self, weapon):
        if self.weapon.base_damage == 0:
            self.weapon = weapon
        else:
            self.pick_up(self.weapon)
            self.weapon = weapon

    def take_on_armor(self, armor):
        if self.armor.base_armor == 0:
            self.armor = armor
        else:
            self.pick_up(self.armor)
            self.armor = armor

    def pick_up(self, item):
        if len(self.inventory) < self.max_slots:
            self.inventory.append(item)
        else:
            print("You can`t pick up this item")

    def buy(self, item):
        if self.coins >= item.cost*2:
            self.coins -= item.cost*2
            print("you have bought a ", item)
        else:
            print("You dont have enough money")
