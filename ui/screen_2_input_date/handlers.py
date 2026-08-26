from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates


@bot.message_handler(state=TravelStates.screen_2_city_input, content_types=["text"])
def message_screen_4_city_input_handler(message: types.Message, state: StateContext):

    city_name = message.text.strip()

    with state.data() as data:
        city_name = data["city_name"]
        city = city_name

    if True:
        show_screen_2_city_input(message.chat.id,state)