from telebot.states.sync.context import StateContext


def get_text_screen_6_travel(state: StateContext):
    with state.data() as data:
        city = data["city"]
        date = data["date"]
        hotel = data["hotel"]
        cafe = data["cafe"]
    return (
        "Вы создали путешествие:\n"
        f"Путешествие в {city} на {date}:\n"
        f"Отель {hotel['name']} с ценой {hotel['price']}$ и сайтом - {hotel['url']}\n"
        f"Кафе {cafe['name']} с ценой {cafe['price']}$ и сайтом - {cafe['url']}"
    )