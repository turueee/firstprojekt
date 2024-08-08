from weather_module import get_current_weather
from value_module import value_moneys
import telebot

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я turueee_bot,
Мои команды:
'/value' - команда запускающая конвертер валют
'/weather' - команда, сообшающая температуру по заданным координатам\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['weather'])
def weather_message(message):
    bot.reply_to(message, 'Введите через пробел свои географические координаты')
    bot.register_next_step_handler(message, weather_me)


def weather_me(message):
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


@bot.message_handler(commands=['value'])
def value_message(message):
    bot.reply_to(message,
                 'Введите через пробел сумму, которую хотите перевести в другую валюту, код валюты, которую хотите перевести, и код валюты, в которую нужно перевести данную сумму.')
    bot.register_next_step_handler(message, value_me)


def value_me(message):
    try:
        s, r, d = message.text.split()
        s = float(s)
    except:
        bot.reply_to(message, 'Данные введены неверно')
    sum_money, Charcode1, Charcode2 = message.text.split()
    try:
        value_moneys(sum_money, Charcode1, Charcode2)
    except:
        bot.reply_to(message, 'Данные введены неверно')
    bot.reply_to(message, value_moneys(sum_money, Charcode1, Charcode2))


bot.infinity_polling()
