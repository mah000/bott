from decouple import config
import telebot


bot_token = config('tokan')

bot = telebot.TeleBot(bot_token)
@bot.message_handlers(commands = ['start','help'])

def welcome(message) :
    bot.send_message(message.chat.id, "حياك الله ")


bot.infinity_polling()



