from telebot.states.sync.context import StateContext
def get_text_screen_6_travel(state:StateContext):

    with state.data() as data:
        date=data["date"]
        city=data["city"]
        cafe=data["cafe"]
        hotel=data["hotel"]

    return f"Вы создали путешествие:\n"\
        f"Путешествие в {city} на {date}:\n"\
            f"Отель {hotel} с ценой (цена выбранного отеля) и сайтом - (сайт выбранного отеля)\n"\
            f"Кафе {cafe} с ценой (цена выбранного кафе) и сайтом - (сайт выбранного кафе)\n"\
            f"Для выхода в любом исходе нажмите - /start"
