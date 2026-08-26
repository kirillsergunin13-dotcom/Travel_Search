import telebot

def get_screen_6_travel_keyboard() -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Сохранить", callback_data="save"
        )
    )

    return keyboard