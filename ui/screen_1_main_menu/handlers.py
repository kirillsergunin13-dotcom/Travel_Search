from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_1_main_menu.texts import get_text_screen_2_input_date
# import datetime

def show_screen_2_input_date(chat_id: int, state: StateContext):

    state.set(TravelStates.screen_2_date_input)
    bot.send_message(
        chat_id,
        get_text_screen_2_input_date(),
    )

@bot.callback_query_handler(state=TravelStates.screen_1_main_menu)
def callback_screen_1_main_menu(call: types.CallbackQuery, state: StateContext):
    print(222)
    bot.answer_callback_query(call.id)
    # date_text = message.text.strip()

    # with state.data() as data:
    #     date = data["date"]
    #     date = datetime(date_text)

    # if True:
    #     show_screen_2_input_date(message.chat.id,state)
    if call.data=="date_input":
        print(111)
        show_screen_2_input_date(call.message.chat.id,state)