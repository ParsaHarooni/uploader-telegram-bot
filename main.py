import importlib
import os
import telebot
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode="MARKDOWN")

def load_plugins(bot):
    for plugin_file in os.listdir('plugins'):
        if plugin_file.endswith('.py'):
            # Remove the .py extension to get the plugin name
            plugin_name = plugin_file[:-3]
            # Import the plugin module
            plugin_module = importlib.import_module('plugins.' + plugin_name)
            # Get the plugin function from the module
            plugin_function = plugin_module.__dict__[plugin_name + '_function']
            # Register the plugin function as a message handler
            bot.message_handler(commands=[plugin_name])(plugin_function)


load_plugins(bot)
bot.infinity_polling()