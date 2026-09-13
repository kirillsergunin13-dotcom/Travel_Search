from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_4_cafe_selection.texts import get_text_screen_5_hotel_selection
from ui.screen_4_cafe_selection.keyboard import get_screen_4_hotel_selection_keyboard


def show_screen_5_hotel_selection(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_5_hotel_selection)
    try:
        with state.data() as data:
            hotels = data.get("hotels", [])
        bot.send_message(
            chat_id,
            get_text_screen_5_hotel_selection(state),
            reply_markup=get_screen_4_hotel_selection_keyboard(hotels),
        )
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")


@bot.callback_query_handler(state=TravelStates.screen_4_cafe_selection)
def callback_screen_4_cafe_selection(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)

    try:
        if not call.data.startswith("cafe_"):
            return
        index = int(call.data.split("_", 1)[1])
        with state.data() as data:
            cafes = data.get("cafes", [])
            if not (0 <= index < len(cafes)):
                bot.send_message(call.message.chat.id, "Ошибка: кафе не найдено, попробуйте ещё раз")
                return
            data["cafe"] = cafes[index]

        show_screen_5_hotel_selection(call.message.chat.id, state)
    except Exception as exc:
        bot.send_message(call.message.chat.id, f"Ошибка: {exc}")