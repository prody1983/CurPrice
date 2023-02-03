import telebot
from params import TOKEN, keys
from extensions import Req_To_Api

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты, цену которой он хочет узнать> \
           <имя валюты, в которой надо узнать цену первой валюты> \
           <количество первой валюты>\nУвидеть список доступных валют: /values'

    bot.reply_to(message, text)

@bot.message_handler(commands=['values', ])
def values(message):
    text = 'Доступные валюты:'

    for key in keys.keys():
        text = '\n'.join((text, key, ))

    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message):
    from_cur, to_cur, amount = message.text.split(' ')

    text = Req_To_Api.get_price(bot, message, from_cur, to_cur, amount)

    bot.send_message(message.chat.id, text)

bot.polling()


