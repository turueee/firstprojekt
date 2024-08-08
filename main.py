import telebot
from telebot import types

from const import API_TOKEN
from weather_module import get_current_weather
from value_module import value_moneys

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton('Погода')
    bt2 = types.KeyboardButton('Конвертер валют')
    markup.add(bt1, bt2)
    bot.send_message(message.chat.id,
                     text="""\
Привет, {0.first_name}! Я turueee_bot
Мои команды""".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def command(message):
    if message.text == 'Погода':
        (bot.send_message(message.chat.id, text='Введите адрес.'))
        bot.register_next_step_handler(message, weather_me)
    elif message.text == 'Конвертер валют':
        (bot.send_message(message.chat.id, text='Введите сумму денег и коды валют'))
        bot.register_next_step_handler(message, value_me)
    else:
        (bot.send_message(message.chat.id, text='Нет такой команды'))


def weather_me(message):
    bot.reply_to(message, get_current_weather(message.text))


def value_me(message):
    sum_money, Charcode1, Charcode2 = message.text.split()
    bot.reply_to(message, value_moneys(sum_money, Charcode1, Charcode2))


bot.infinity_polling()
