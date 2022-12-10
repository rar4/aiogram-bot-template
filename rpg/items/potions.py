class HpPotion:
    def __init__(self):
        self.cost = 0
        self.hp_up = 0

    def use(self, player):

        player.healgh += self.hp_up

        if player.healgh > player.Max_healgh:
            player.healgh = player.Max_healgh
            player.inventory.remove(self)
        return "You have used potion"


class LitlHpPotion(HpPotion):
    def __init__(self):
        super().__init__()
        self.cost = 10
        self.hp_up = 20

    def __str__(self):
        return "litl hp potion"


class MidHpPotion(HpPotion):
    def __init__(self):
        super().__init__()
        self.cost = 20
        self.hp_up = 50

    def __str__(self):
        return "Medium hp potion"


class BigHpPotion(HpPotion):
    def __init__(self):
        super().__init__()
        self.cost = 50
        self.hp_up = 100

    def __str__(self):
        return "Big hp potion"
