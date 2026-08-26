import telebot

def get_screen_8_old_travel_keyboard() -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Просмотреть более новое", callback_data="up"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Просмотреть более старое", callback_data="down"
        )
    )
    return keyboard