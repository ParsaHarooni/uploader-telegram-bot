import telebot
import os


token = os.environ.get('TOKEN')
bot = telebot.TeleBot(token, parse_mode="MARKDOWN")