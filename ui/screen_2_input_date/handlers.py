from datetime import datetime

from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_2_input_date.texts import get_date_error_text, get_text_screen_3_input_city


def show_screen_3_input_city(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_3_city_input)
    bot.send_message(
        chat_id,
        get_text_screen_3_input_city(state),
    )


@bot.message_handler(state=TravelStates.screen_2_date_input, content_types=["text"])
def message_screen_2_date_input(message: types.Message, state: StateContext):

    date_text = message.text.strip()
    try:
        parsed = datetime.strptime(date_text, "%d.%m.%Y").date()
    except ValueError:
        bot.send_message(message.chat.id, get_date_error_text())
        bot.send_message(
            message.chat.id,
            "Вы создаёте новое путешествие:\n"
            "Введите пожалуйста дату вашего путешествия в виде день.месяц.год",
        )
        return
    except Exception as exc:
        bot.send_message(message.chat.id, f"Ошибка: {exc}")
        return

    with state.data() as data:
        data["date"] = parsed.strftime("%d.%m.%Y")
        data["date_iso"] = parsed.isoformat()

    show_screen_3_input_city(message.chat.id, state)