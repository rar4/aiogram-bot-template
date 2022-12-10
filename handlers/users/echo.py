from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db

from rpg import main

from rpg.utilities import loader

from states.gamestates import UserState

from keyboards import inline

from rpg.utilities.loader import player as pleyer

import time


@dp.message_handler(commands=["addcoins"], is_admin = True)
async def add(message: types.Message):
    try:
        a = int(message.text.split()[-1])
        loader.player.coins += a
    except:
        await message.answer("wrong syntax")


@dp.message_handler(commands=['fight'])
async def fight(message: types.Message, state: FSMContext):
    mob = loader.rat


    await message.answer('rat is approaching')
    img = types.InputFile("media/eee.jpg")
    await message.answer_photo(img)
    m = f"""____________________________________________________________________________
    your healgh is: ", {pleyer.healgh}
    enemy`s healgh is: ", {mob.healgh}
        ____________________________________________________________________________"""

    await message.answer(m)

    await message.answer("what do you want to do", reply_markup=inline.uskey)

    await UserState.combat.set()

    await state.update_data({"mob": mob})


@dp.callback_query_handler(state=UserState.combat)
async def fight2(message: types.CallbackQuery, state: FSMContext):
    mob = await state.get_data("mob")

    mob = mob["mob"]

    a = message.data

    print(a)
    if a == '1':
        dmg1 = pleyer.attack(mob)
        await message.message.answer(f"you have made {dmg1} damage")
        dmg2 = mob.attack(pleyer)
        await message.message.answer(f"rat has made {dmg2} damage")

        await message.message.answer("SSSSSSSSIIIIIIIIIIIIII")

        if pleyer.healgh > 0 and mob.healgh > 0:

            await message.message.answer("SSSSSSSSIIIIIIIIIIIIII   2")

            m = f"""____________________________________________________________________________
                    your healgh is: ", {pleyer.healgh}
                    enemy`s healgh is: ", {mob.healgh}
                        ____________________________________________________________________________"""

            await message.message.answer(m)

            await state.update_data({"mob": mob})

            await message.message.answer("what do you want to do", reply_markup=inline.uskey)

        else:
            await message.message.answer("SSSSSSSSIIIIIIIIIIIIII       3")

            await endcombat(message.message, state, message.message.text)
            await state.finish()

    elif a == '2':
        mob.attack(pleyer)
        await state.finish()
        await message.message.answer('You have run away')
        return
    elif a == "?":
        await message.message.answer("""attack - you attack monster and monster attacks you,
        run away - you run away """)
    elif a == "st":
        await status(message.message)


async def endcombat(message: types.message, state: FSMContext, a):
    mob = await state.get_data("mob")

    mob = mob["mob"]

    if pleyer.healgh > 0:
        if a == '1':



            ee = f"""you have killed rat
            ----------------------------------------------------------------------------------------------
            you have found"""

            await message.answer(ee)

            await mob.loot(pleyer, message)


    else:
        await message.answer("You have been died")


@dp.callback_query_handler(state=UserState.inventory)
async def button_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "esc":
        await state.finish()
    else:
        a = loader.player.inventory[int(callback.data)]

        if str(a).split()[-1] == 'potion':
            await callback.answer(a.use(loader.player))
        elif str(a).split()[-1] == 'armor':
            loader.player.take_on_armor(a)
            await callback.answer(f"You have picked up {str(a)}")
        else:
            loader.player.take_on_weapon(a)
            await callback.answer(f"You have picked up {str(a)}")


@dp.message_handler(commands=['inventory'])
async def inventory(message: types.Message):
    await message.answer(main.status(loader.player))
    await UserState.inventory.set()
    await message.answer("Do you want to use something", reply_markup=inline.user_keybords())


@dp.message_handler(commands=['status'])
async def status(message: types.Message):
    await message.answer(main.status(loader.player))



@dp.message_handler(commands=['load'])
async def load(message: types.Message):
    db.load(message.from_user.id)
    await message.answer("you have been loaded")


@dp.message_handler(commands=['save'])
async def save(message: types.Message):
    db.save(loader.player.coins, message.from_user.id)
    await message.answer("you have been saved")



