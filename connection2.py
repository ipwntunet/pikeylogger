from telebot import TeleBot

# Set here the Telegram bot token
BOT_TOKEN = "7876214628:AAHeWHhi9SvSUPnYhZ2_Q-wBL7JjirGnbW0"
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Ok it works")

bot.infinity_polling()
