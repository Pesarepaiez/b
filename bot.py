import os
import telebot
from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Your Telegram Bot Token
BOT_TOKEN = "8058388234:AAH1E2l5kS5g4Vmv0XCthqN3H_bSdqmIPkI"
bot = telebot.TeleBot(BOT_TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the simple Telegram bot!")

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

# Set webhook
WEBHOOK_URL = "https://dic-bot-production.up.railway.app"
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

# Start Flask server
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=int(os.getenv('PORT', 5000)))
