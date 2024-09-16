#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import APY_KEY

API_TOKEN = APY_KEY

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)
#     bot.send_message(message.chat.id, "Привет1")

def f(message):
    if (message.text.splitlines()[0] == 'Мерки') or (message.text.splitlines()[0] == 'мерки'):
        return message
    bot.send_message(message.chat.id, "Для расчетов напишите Мерки в начале сообщения")

@bot.message_handler(func= f)
def myFunk(message):
    if message.text != "Falce":
        bot.send_message(message.chat.id, "Мерки приняты")
        answer = message.text.splitlines()
        counMeasure = len(answer) - 1
        bot.send_message(message.chat.id, "Количество мерок: " + str(counMeasure))






bot.infinity_polling()