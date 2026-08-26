from telebot.states.sync.context import StateContext #{state.data["date"]}

def get_text_screen_3_input_city(state:StateContext):
    with state.data() as data:
            date=data["date"]
    return f"Вы создаёте новое путешествие на {date} :\n"\
           "Введите пожалуйста город вашего путешествия"