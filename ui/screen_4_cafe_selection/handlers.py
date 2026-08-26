from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_4_cafe_selection.texts import get_text_screen_5_hotel_selection
from ui.screen_4_cafe_selection.keyboard import get_screen_4_hotel_selection_keyboard

def show_screen_5_hotel_selection(chat_id:int,state:StateContext):
    state.set(TravelStates.screen_5_hotel_selection)
    bot.send_message(
        chat_id,
        get_text_screen_5_hotel_selection(state),
        reply_markup=get_screen_4_hotel_selection_keyboard(),
    )

@bot.callback_query_handler(state=TravelStates.screen_4_cafe_selection)
def callback_screen_4_cafe_selection(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)

    with state.data() as data:
        data["cafe"]=call.data
    
    show_screen_5_hotel_selection(call.message.chat.id,state)
