from rpg.mobs.mob import Mob

import random

from rpg.utilities import loader


class Rat(Mob):
    def __init__(self):
        super().__init__()
        self.healgh = 20
        self.real_damage = 5
        self.real_armor = 5

    @staticmethod
    async def loot(player, message):
        player.coins += random.randint(0, 10)

        a = random.randint(1, 4)

        if a == 2:
            b = random.randint(1, 10)
            if b in [1, 2, 2, 3, 4]:
                player.pick_up(loader.mid_hp_potion)
                await message.answer(loader.mid_hp_potion)
            elif b in [5, 6, 7]:
                player.pick_up(loader.litl_hp_potion)
                await message.answer(loader.litl_hp_potion)
            elif b in [8, 9]:
                player.pick_up(loader.big_hp_potion)
                await message.answer(loader.big_hp_potion)
            else:
                q = loader.short_sword()
                player.pick_up(q)
                await message.answer(q)
        else:
            await message.answer('Nothing')
        await message.answer(f'{player.coins} coins')
