from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from rpg.utilities import loader


def user_keybords():
    s = 0

    c = []

    for i in loader.player.inventory:
        c.append([InlineKeyboardButton(str(s), callback_data=str(s))])

    d = [InlineKeyboardButton("escape", callback_data="esc")]

    c.append(d)

    return InlineKeyboardMarkup(inline_keyboard=c)


uskey = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("attack", callback_data="1"),
                                               InlineKeyboardButton("run away", callback_data="2"),
                                               InlineKeyboardButton("status", callback_data="st"),
                                               InlineKeyboardButton("info", callback_data="?")]])
