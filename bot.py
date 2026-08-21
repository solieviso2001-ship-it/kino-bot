import os
import telebot

TOKEN = os.getenv("8803268527:AAEu_1NHazYZoqPTq82cRKQvD3RomOhVMoE")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "🎬 Kino botiga xush kelibsiz!")

print("Bot ishga tushdi...")
bot.infinity_polling()
