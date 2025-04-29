from telegram import KeyboardButton, ReplyKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes

TOKEN = '7764959521:AAH0v27Vzwh_wO_iibzJ5ilhhlpEszf1A4I'  # ← Сенің токенің

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(
            text="📖 Оқуды бастау",
            web_app=WebAppInfo(url="https://6810b33bb8002019e1752b90--bejewelled-pika-0b7c99.netlify.app/")
        )]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "📚 Оқу уақыты басталды!\nТөмендегі батырманы басыңыз:",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()

