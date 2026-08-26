from telebot import types
from telebot.states.sync.context import StateContext
from bot_instence import bot
from ui.states import TravelStates
from ui.screen_5_hotel_selection.texts import get_text_screen_6_travel
from ui.screen_5_hotel_selection.keyboard import get_screen_6_travel_keyboard

def show_screen_6_travel(chat_id:int,state:StateContext):
    state.set(TravelStates.screen_6_travel)
    bot.send_message(
        chat_id,
        get_text_screen_6_travel(state),
        reply_markup=get_screen_6_travel_keyboard(),
    )


@bot.callback_query_handler(state=TravelStates.screen_5_hotel_selection)
def callback_screen_5_hotel_selection(call: types.CallbackQuery, state: StateContext):

    bot.answer_callback_query(call.id)

    with state.data() as data:
        data["hotel"]=call.data

    show_screen_6_travel(call.message.chat.id,state)