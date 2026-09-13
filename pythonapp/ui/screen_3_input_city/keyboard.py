import telebot


def get_screen_3_cafe_selection_keyboard(cafes) -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    for index, cafe in enumerate(cafes):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"{cafe['tier']} кафе {cafe['name']} с средней ценой {cafe['price']}$",
                callback_data=f"cafe_{index}",
            )
        )
    return keyboard