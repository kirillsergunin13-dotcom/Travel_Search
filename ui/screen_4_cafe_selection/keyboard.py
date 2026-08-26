import telebot

def get_screen_4_hotel_selection_keyboard() -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Дешёвое отель 'дешёвка' с ценой 8800303535$", callback_data="one_hotel"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Обычное отель 'нормалды' с ценой 0101010101$", callback_data="two_hotel"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Дорогое отель 'дорогоогого' с ценой 99999999999999999$", callback_data="three_hotel"
        )
    )
    print(111)
    return keyboard