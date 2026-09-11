import telebot


def get_screen_4_hotel_selection_keyboard(hotels) -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    for index, hotel in enumerate(hotels):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"{hotel['tier']} отель {hotel['name']} с средней ценой {hotel['price']}$",
                callback_data=f"hotel_{index}",
            )
        )
    return keyboard