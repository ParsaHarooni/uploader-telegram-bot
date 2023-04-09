from plugins.utils import texts
from plugins.utils.bot import bot

def start_function(msg):
    bot.send_message(chat_id=msg.chat.id, text=texts.start)
