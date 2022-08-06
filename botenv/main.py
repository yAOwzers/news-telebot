import os
import telebot
from dotenv import load_dotenv

import scrapper

load_dotenv()

API_KEY = os.getenv("API_KEY")
load_dotenv()
bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=["get_cna"])
def hello(message):
  response = scrapper.scrape()
  bigNewsText = ""
  for news in response:
    bigNewsText = bigNewsText + news + "\n\n"
  bot.send_message(message.chat.id, bigNewsText)

bot.infinity_polling()