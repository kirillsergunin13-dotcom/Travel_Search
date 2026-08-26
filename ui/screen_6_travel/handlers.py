from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_6_travel.texts import get_save_text

def print_save_text(chat_id:int):
    bot.send_message(chat_id,get_save_text())

@bot.callback_query_handler(state=TravelStates.screen_6_travel)
def callback_screen_6_travel(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    if call.data=="save":
        print_save_text(call.message.chat.id)