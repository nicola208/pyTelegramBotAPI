#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '1595206639:AAGDTFg_xRpHh6q9wjYV-JSESN9MZLyvuks'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao io sono il bot del gruppo"STW_Nico*_* e STW_Gionny.
Sono stato appena creato per gestire il gruppo😅\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if.message.text=='Ciao':
        bot.reply_to(message, Ciao sono un bot,come stai?')
    elif message.text=='niente':
        bot.reply_to(message, 'Bene mi fa piacere. Anche io ok!')
    elise:
        bot.reply_to(message, 'Sono stato appena creato e non capisco tutti i messaggi.Prova a scrivermi altro.')
bot.polling()
