from telebot.states.sync.context import StateContext


def get_text_screen_2_input_date():
    return (
        "Вы создаёте новое путешествие:\n"
        "Введите пожалуйста дату вашего путешествия в виде день.месяц.год"
    )


def get_text_screen_8_old_travel(state: StateContext):
    with state.data() as data:
        cards = data.get("travel_cards", [])
        index = data.get("olding", 0)
    if not cards:
        return (
            "У вас пока нет сохранённых путешествий.\n"
            "Нажмите «Выход на главный экран», чтобы вернуться в меню."
        )
    return cards[index]