from telebot.states.sync.context import StateContext
def get_text_screen_5_hotel_selection(state:StateContext):
    with state.data() as data:
        date=data["date"]
        city=data["city"]

    return f"Вы создаёте новое путешествие на {date} в {city} :\n"\
           "Выберете пожалуйста отеля вашего путешествия:"