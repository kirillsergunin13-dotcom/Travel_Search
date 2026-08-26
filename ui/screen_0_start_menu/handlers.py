"""Обработчик команды ``/start`` и функция показа главного меню."""

from telebot import types
from telebot.states.sync.context import StateContext

from bot_instence import bot
from ui.screen_0_start_menu.keyboard import get_screen_0_start_menu_keyboard
from ui.screen_0_start_menu.texts import get_screen_0_start_menu_text
from ui.states import TravelStates


def show_screen_1_main_menu(chat_id: int, state: StateContext):

    state.set(TravelStates.screen_1_main_menu)
    bot.send_message(
        chat_id,
        get_screen_0_start_menu_text(),
        reply_markup=get_screen_0_start_menu_keyboard(),
    )


@bot.message_handler(commands=["start"])
def command_screen_0_start_handler(message: types.Message, state: StateContext):
    state.delete()

    show_screen_1_main_menu(message.chat.id, state)