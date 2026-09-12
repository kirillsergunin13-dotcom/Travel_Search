from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from bot_instence import bot
from models.database import Base, engine

import models.treavels  
import ui.screen_0_start_menu.handlers
import ui.screen_1_main_menu.handlers
import ui.screen_2_input_date.handlers
import ui.screen_3_input_city.handlers
import ui.screen_4_cafe_selection.handlers
import ui.screen_5_hotel_selection.handlers
import ui.screen_6_travel.handlers

try:
    Base.metadata.create_all(engine)
except Exception as exc:
    print(f"Не удалось создать таблицы БД: {exc}")

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

print("TravelHunter запущен")
bot.infinity_polling()