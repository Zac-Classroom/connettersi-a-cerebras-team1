from dotenv import dotenv_values
import telebot

config = dotenv_values(".env")
print(config)

bot = telebot.TeleBot(config["TELEGRAM"])

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    bot.reply_to(message, "Ciao sono Davis")

bot.polling()