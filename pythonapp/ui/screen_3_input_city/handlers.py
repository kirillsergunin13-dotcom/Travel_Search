from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from services.search_service import SearchPlaceError, SearchPlaceService
from ui.states import TravelStates
from ui.screen_3_input_city.texts import get_text_screen_4_cafe_selection
from ui.screen_3_input_city.keyboard import get_screen_3_cafe_selection_keyboard

search_service = SearchPlaceService()


def show_screen_4_cafe_selection(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_4_cafe_selection)
    try:
        with state.data() as data:
            cafes = data.get("cafes", [])
        bot.send_message(
            chat_id,
            get_text_screen_4_cafe_selection(state),
            reply_markup=get_screen_3_cafe_selection_keyboard(cafes),
        )
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")


@bot.message_handler(state=TravelStates.screen_3_city_input, content_types=["text"])
def message_screen_3_city_input(message: types.Message, state: StateContext):

    city_text = message.text.strip()
    if not city_text:
        bot.send_message(message.chat.id, "Ошибка! Введите корректное название города.")
        return

    try:
        valid, error = search_service.check_city(city_text)
        if not valid:
            bot.send_message(message.chat.id, error)
            bot.send_message(message.chat.id, "Введите пожалуйста город вашего путешествия")
            return

        hotels = search_service.get_hotels(city_text)
        cafes = search_service.get_cafes(city_text)

        with state.data() as data:
            data["city"] = city_text
            data["cafes"] = [c.to_dict() for c in cafes]
            data["hotels"] = [h.to_dict() for h in hotels]

        show_screen_4_cafe_selection(message.chat.id, state)

    except SearchPlaceError as exc:
        bot.send_message(message.chat.id, f"Ошибка: {exc}")
        bot.send_message(message.chat.id, "Введите пожалуйста город вашего путешествия")
    except Exception as exc:
        bot.send_message(message.chat.id, f"Ошибка: {exc}")
        bot.send_message(message.chat.id, "Введите пожалуйста город вашего путешествия")