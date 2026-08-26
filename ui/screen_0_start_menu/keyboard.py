import telebot

def get_screen_0_start_menu_keyboard() -> telebot.types.InlineKeyboardMarkup:

    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Просмотреть прошлые путешествия", callback_data="screen_1_show_travel"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Создать новое путешествие", callback_data="date_input"
        )
    )
    return keyboard