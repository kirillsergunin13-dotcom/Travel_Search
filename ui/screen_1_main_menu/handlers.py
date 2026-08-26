from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_1_main_menu.texts import get_text_screen_2_input_date,get_text_screen_8_old_travel
from ui.screen_1_main_menu.keyboard import get_screen_8_old_travel_keyboard

def show_screen_2_input_date(chat_id: int, state: StateContext):

    state.set(TravelStates.screen_2_date_input)
    bot.send_message(
        chat_id,
        get_text_screen_2_input_date(),
    )

def show_screen_8_old_travel(chat_id:int, state: StateContext):
    
    state.set(TravelStates.screen_8_old_travel)
    bot.send_message(
        chat_id,
        get_text_screen_8_old_travel(state),
        reply_markup=get_screen_8_old_travel_keyboard(),
    )

@bot.callback_query_handler(state=TravelStates.screen_1_main_menu)
def callback_screen_1_main_menu(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)
    
    if call.data=="date_input":
        show_screen_2_input_date(call.message.chat.id,state)
    elif call.data=="old_travel":
        with state.data() as data:
            data["olding"]=0
        show_screen_8_old_travel(call.message.chat.id,state)



@bot.callback_query_handler(state=TravelStates.screen_8_old_travel)
def callback_screen_8_old_travel(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)
    
    if call.data=="down":
        with state.data() as data:
            data["olding"]-=1
        show_screen_8_old_travel(call.message.chat.id,state)
    elif call.data=="up":
        with state.data() as data:
            data["olding"]+=1
        show_screen_8_old_travel(call.message.chat.id,state)