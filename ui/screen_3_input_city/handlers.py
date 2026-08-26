from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_3_input_city.texts import get_text_screen_4_cafe_selection
from ui.screen_3_input_city.keyboard import get_screen_3_cafe_selection_keyboard

def show_screen_4_cafe_selection(chat_id:int,state:StateContext):
    state.set(TravelStates.screen_4_cafe_selection)
    bot.send_message(
        chat_id,
        get_text_screen_4_cafe_selection(state),
        reply_markup=get_screen_3_cafe_selection_keyboard(),
    )

@bot.message_handler(state=TravelStates.screen_3_city_input, content_types=["text"])
def message_screen_3_city_input(message: types.Message, state: StateContext):

    city_text = message.text.strip()
    with state.data() as data:
                data["city"]= city_text

    if city_text!="":
        show_screen_4_cafe_selection(message.chat.id,state)
        