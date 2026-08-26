from telebot.states import State, StatesGroup

class TravelStates(StatesGroup):
    
    screen_1_main_menu = State()
    
    screen_2_date_input = State()
    
    screen_3_city_input = State()
    
    screen_4_cafe_selection = State()
    
    screen_5_hotel_selection = State()
    
    screen_6_travel = State()
    
    screen_8_old_travel = State()
    