from telebot.states.sync.context import StateContext
def get_text_screen_2_input_date():
    return "Вы создаёте новое путешествие:\n"\
           "Введите пожалуйста дату вашего путешествия в виде день.месяц.год"
def get_text_screen_8_old_travel(state:StateContext):

    with state.data() as data:
        olding=data["olding"]
    return f"По близости (от старых к новым) {olding} Здесь типо путешествие Вернуться - /start"