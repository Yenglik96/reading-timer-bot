from flask import Flask, request
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")  # Render Secret арқылы сақта
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")   # Render-ге толық URL ретінде енгіз (мысалы: https://your-app.onrender.com)

app = Flask(__name__)
bot = Bot(token=TOKEN)

keyboard = [
    [KeyboardButton(
        text="📖 Оқуды бастау",
        web_app=WebAppInfo(url="https://сенің-netlify-сайтың.netlify.app/")
    )]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.process_update(update)
    return "OK", 200


@app.route("/")
def home():
    return "Бот жұмыс істеп тұр."


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Оқу уақыты басталды!\nТөмендегі батырманы басыңыз:",
        reply_markup=reply_markup
    )


if __name__ == "__main__":
    bot.delete_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
