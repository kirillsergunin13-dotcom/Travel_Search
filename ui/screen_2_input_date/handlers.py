from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_2_input_date.texts import get_text_screen_3_input_city
import datetime

def show_screen_3_input_city(chat_id:int,state:StateContext):
    state.set(TravelStates.screen_3_city_input)
    bot.send_message(
        chat_id,
        get_text_screen_3_input_city(state),
    )

@bot.message_handler(state=TravelStates.screen_2_date_input, content_types=["text"])
def message_screen_2_date_input(message: types.Message, state: StateContext):

    date_text = message.text.strip()
    with state.data() as data:
                data["date"]= date_text

    if date_text!="":
        show_screen_3_input_city(message.chat.id,state)
        