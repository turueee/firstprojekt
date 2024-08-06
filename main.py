from weather_module import get_current_weather
import telebot


# API_TOKEN = '7278848607:AAG6PS3r_eg_xBtRRBC3Wp1czzMLRSHSBmw'
# bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я turueee_bot, я сообщаю текущуюю температуру.
Введите координаты без запятых через пробела.\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    try:
        s, r = map(float, message.text.split())
    except:
        bot.reply_to(message, 'Координаты введены неправильно!')
    latitude, longitude = map(float, message.text.split())
    try:
        get_current_weather(latitude, longitude)
    except:
        bot.reply_to(message, 'Введены несуществующие координаты!')
    bot.reply_to(message, get_current_weather(latitude, longitude))


bot.infinity_polling()
