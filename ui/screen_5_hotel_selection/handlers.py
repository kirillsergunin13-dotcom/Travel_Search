from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_5_hotel_selection.texts import get_text_screen_6_travel
from ui.screen_5_hotel_selection.keyboard import get_screen_6_travel_keyboard


def show_screen_6_travel(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_6_travel)
    try:
        bot.send_message(
            chat_id,
            get_text_screen_6_travel(state),
            reply_markup=get_screen_6_travel_keyboard(),
        )
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")


@bot.callback_query_handler(state=TravelStates.screen_5_hotel_selection)
def callback_screen_5_hotel_selection(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)

    try:
        if not call.data.startswith("hotel_"):
            return
        index = int(call.data.split("_", 1)[1])
        with state.data() as data:
            hotels = data.get("hotels", [])
            if not (0 <= index < len(hotels)):
                bot.send_message(call.message.chat.id, "Ошибка: отель не найден, попробуйте ещё раз")
                return
            data["hotel"] = hotels[index]

        show_screen_6_travel(call.message.chat.id, state)
    except Exception as exc:
        bot.send_message(call.message.chat.id, f"Ошибка: {exc}")