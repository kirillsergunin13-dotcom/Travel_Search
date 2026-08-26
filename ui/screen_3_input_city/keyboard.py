import telebot

def get_screen_3_cafe_selection_keyboard() -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Дешёвое кафе 'дешёвка' с ценой 8800303535$", callback_data="one_cafe"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Обычное кафе 'нормалды' с ценой 0101010101$", callback_data="two_cafe"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Дорогое кафе 'дорогоогого' с ценой 99999999999999999$", callback_data="three_cafe"
        )
    )
    return keyboard