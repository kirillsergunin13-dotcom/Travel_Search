import telebot


def get_screen_8_old_travel_keyboard(has_travels: bool = False) -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    if has_travels:
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
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                "Удалить", callback_data="delete"
            )
        )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Выход на главный экран", callback_data="exit"
        )
    )
    return keyboard