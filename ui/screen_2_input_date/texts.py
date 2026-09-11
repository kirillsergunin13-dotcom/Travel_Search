from telebot.states.sync.context import StateContext


def get_text_screen_3_input_city(state: StateContext):
    with state.data() as data:
        date = data["date"]
    return (
        f"Вы создаёте новое путешествие на {date} :\n"
        "Введите пожалуйста город вашего путешествия"
    )


def get_date_error_text():
    return (
        "Ошибка! Дата введена неверно.\n"
        "Нужно вводить дату в виде день.месяц.год (например, 25.12.2026).\n"
        "Попробуйте ещё раз."
    )