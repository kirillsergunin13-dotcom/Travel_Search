from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from services.travel_service import TravelService, TravelServiceError
from ui.screen_0_start_menu.handlers import show_screen_1_main_menu
from ui.states import TravelStates
from ui.screen_1_main_menu.texts import get_text_screen_2_input_date, get_text_screen_8_old_travel
from ui.screen_1_main_menu.keyboard import get_screen_8_old_travel_keyboard

travel_service = TravelService()


def show_screen_2_input_date(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_2_date_input)
    try:
        bot.send_message(chat_id, get_text_screen_2_input_date())
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")


def show_screen_8_old_travel(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_8_old_travel)
    try:
        travels = travel_service.get_user_travels(chat_id)
        cards = [travel_service.format_saved_travel(t) for t in travels]
        with state.data() as data:
            data["olding"] = 0
            data["travel_cards"] = cards
            data["travel_ids"] = [t.id for t in travels]
        bot.send_message(
            chat_id,
            get_text_screen_8_old_travel(state),
            reply_markup=get_screen_8_old_travel_keyboard(bool(cards)),
        )
    except TravelServiceError as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")
        show_screen_1_main_menu(chat_id, state)
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")
        show_screen_1_main_menu(chat_id, state)


@bot.callback_query_handler(state=TravelStates.screen_1_main_menu)
def callback_screen_1_main_menu(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)

    if call.data == "date_input":
        show_screen_2_input_date(call.message.chat.id, state)
    elif call.data == "old_travel":
        show_screen_8_old_travel(call.message.chat.id, state)


@bot.callback_query_handler(state=TravelStates.screen_8_old_travel)
def callback_screen_8_old_travel(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)
    chat_id = call.message.chat.id

    try:
        with state.data() as data:
            cards = data.get("travel_cards", [])
            ids = data.get("travel_ids", [])
            index = data.get("olding", 0)

        if call.data == "up" and cards:
            index = min(len(cards) - 1, index + 1)
        elif call.data == "down" and cards:
            index = max(0, index - 1)
        elif call.data == "delete" and ids:
            travel_service.delete_travel(call.from_user.id, ids[index])
            travels = travel_service.get_user_travels(call.from_user.id)
            cards = [travel_service.format_saved_travel(t) for t in travels]
            ids = [t.id for t in travels]
            index = max(0, min(index, len(cards) - 1))
            with state.data() as data:
                data["travel_cards"] = cards
                data["travel_ids"] = ids
            if not cards:
                bot.send_message(chat_id, "Путешествие удалено. Сохранённых путешествий больше нет.")
                show_screen_1_main_menu(chat_id, state)
                return
        elif call.data == "exit":
            show_screen_1_main_menu(chat_id, state)
            return

        with state.data() as data:
            data["olding"] = index
        bot.edit_message_text(
            get_text_screen_8_old_travel(state),
            chat_id,
            call.message.message_id,
            reply_markup=get_screen_8_old_travel_keyboard(bool(cards)),
        )
    except TravelServiceError as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")
    except Exception as exc:
        bot.send_message(chat_id, f"Ошибка: {exc}")