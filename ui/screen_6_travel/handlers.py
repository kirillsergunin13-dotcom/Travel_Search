from datetime import date

from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from services.travel_service import TravelService, TravelServiceError
from ui.screen_0_start_menu.handlers import show_screen_1_main_menu
from ui.states import TravelStates
from ui.screen_6_travel.texts import get_save_text

travel_service = TravelService()


@bot.callback_query_handler(state=TravelStates.screen_6_travel)
def callback_screen_6_travel(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id

    try:
        if call.data == "save":
            with state.data() as data:
                city = data["city"]
                travel_date = date.fromisoformat(data["date_iso"])
                hotel = data["hotel"]
                cafe = data["cafe"]

            travel_service.save_travel(call.from_user.id, city, travel_date, hotel, cafe)
            bot.send_message(chat_id, get_save_text())
            show_screen_1_main_menu(chat_id, state)
    except TravelServiceError as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")