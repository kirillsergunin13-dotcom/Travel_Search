"""Обработчики стартового экрана и главного меню."""

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instence import bot
from ui.screen_0_start_menu.keyboard import get_main_menu_keyboard, get_start_keyboard
from ui.screen_0_start_menu.texts import get_main_menu_text, get_screen_0_start_menu_text
from ui.states import TravelStates


def send_error(chat_id: int, exc: Exception):
    bot.send_message(chat_id, f"Ошибка: {exc}")


def show_screen_0_start_menu(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_0_start_menu)
    try:
        bot.send_message(
            chat_id,
            get_screen_0_start_menu_text(),
            reply_markup=get_start_keyboard(),
        )
    except Exception as exc:
        send_error(chat_id, exc)


def show_screen_1_main_menu(chat_id: int, state: StateContext):
    state.set(TravelStates.screen_1_main_menu)
    try:
        bot.send_message(
            chat_id,
            get_main_menu_text(),
            reply_markup=get_main_menu_keyboard(),
        )
    except Exception as exc:
        send_error(chat_id, exc)


@bot.message_handler(commands=["start"])
def command_screen_0_start_handler(message: types.Message, state: StateContext):
    state.delete()
    show_screen_0_start_menu(message.chat.id, state)


@bot.callback_query_handler(func=lambda call: call.data == "start")
def callback_start_handler(call: types.CallbackQuery, state: StateContext):
    try:
        bot.answer_callback_query(call.id)
    except Exception:
        pass
    show_screen_1_main_menu(call.message.chat.id, state)