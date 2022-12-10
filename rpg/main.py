from .utilities import loader

import time

import random
from rpg.mobs import player, mobes


def list_of_items(items):
    a = 0
    string = ''
    for item in items:
        strin = f"{a}   {item}\n"
        string += strin
    return string


def status(pleyer: player.Player):
    return f"""Status: 
        Hp: , {pleyer.healgh}
        Damage: , {pleyer.real_damage}
        Weapon: , {pleyer.weapon}
        Armor: , {pleyer.armor}
        Coins: ,{pleyer.coins}
    ------------------------------------------------------------------------------
    You have: 
    {list_of_items(pleyer.inventory)}"""


def inventory(pleyer):
    if pleyer.inventory:
        b = "."
        while b != 'esc':
            status(pleyer)
            print('--------------------------------------------------------------------------------------------')
            b = input("do you want to use something?  "
                      "\n (to use item inpunt it`s number) \n\n (to quit input \"esc\"): ")

            try:
                b = int(b)
                pleyer.inventory[b].use(loader.player)
            except ValueError and IndexError:
                if b == "esc":
                    break
                else:
                    pass
    else:
        print("You don`t have anything in your inventory")


def mob_combat(pleyer: player.Player, mob: mobes.Rat):
    print()
    print()
    print('rat is approaching')
    while pleyer.healgh > 0 and mob.healgh > 0:
        print("____________________________________________________________________________")
        print("your healgh is: ", pleyer.healgh)
        print("enemy`s healgh is: ", mob.healgh)
        print("____________________________________________________________________________")

        a = input("what do you want to do (1 - attack, 2 - run away, ? - info, inv - inventory, st - status)")

        if a == '1':
            dmg1 = pleyer.attack(mob)
            print(f"you have made {dmg1} damage")
            dmg2 = mob.attack(pleyer)
            print(f"rat has made {dmg2} damage")
        elif a == '2':
            mob.attack(pleyer)
            break
        elif a == "?":
            print("""attack - you attack monster and monster attacks you,
        run away - monster attacks you and you run away """)
        elif a == "inv":
            inventory(pleyer)
        elif a == "st":
            status(pleyer)

        time.sleep(1)

    if pleyer.healgh > 0:
        if a == '1':
            print("you have killed rat")
            print("-----------------------------------------------------------------------------------------------")
            print("you have found")
            print()
            f = mob.loot(pleyer)
            print()
            print('and', f, "coins")

        else:
            print("you have run away from rat")
    else:
        print("You have been died")


def trader(pleyer):
    a = 0
    print("You have mat a trader")
    print()
    print("you have", pleyer.coins, "coins")
    list_of_goods = [loader.litl_hp_potion, loader.mid_hp_potion, loader.big_hp_potion, loader.short_sword(),
                     loader.leather_armor()]
    print("-----------------------------------------------------------------------------------------------------------")

    print("He has")
    print()

    for i in list_of_goods:
        print(a, i, ", ", i.cost*2, 'coins')
        print()
        a += 1
    print("-----------------------------------------------------------------------------------------------------------")
    c = ""

    while c != 'esc':
        print()
        c = input("What do you want to by   (to by something you have to input its number,  to escape input esc): ")

        try:
            c = int(c)
            if c < len(list_of_goods):
                pleyer.buy(list_of_goods[c])
        except ValueError:
            pass


def game_loop():
    a = random.randint(1, 4)

    if a in range(1, 3):
        mob_combat(loader.player, loader.rat)
    else:
        trader(loader.player)


def main():
    name = input("input your name: ")
    print("Hi", name)

    a = ''

    while a != "quit":
        a = input("What do you want to do (h - help): ")

        if a == 'h':
            print('---------------------------------------------------------------------------------------------------')
            print('e - explore world, \n inv - inventory, \n quit - escape from the game,\n st - status')
            print("---------------------------------------------------------------------------------------------------")
        elif a == 'e':
            game_loop()
        elif a == 'inv':
            inventory(loader.player)
        elif a == 'st':
            status(loader.player)




