import os
import telebot
from dotenv import load_dotenv

import Scrapper
import HelpMessage

load_dotenv()

API_KEY = os.getenv("API_KEY")
load_dotenv()
bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
  helpMessage = HelpMessage.sendHelp()
  bot.send_message(message.chat.id, helpMessage)

@bot.message_handler(commands=["get_cna"])
def hello(message):
  response = Scrapper.scrape()
  bigNewsText = ""
  for news in response:
    bigNewsText = bigNewsText + news + "\n\n"
  bot.send_message(message.chat.id, bigNewsText)

bot.infinity_polling()