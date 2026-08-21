import os
import telebot
from flask import Flask, request

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Kino bot ishlayapti!"

@app.route("/webhook", methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "🎬 Kino botiga xush kelibsiz!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
