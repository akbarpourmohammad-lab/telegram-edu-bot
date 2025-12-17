from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

menu = ReplyKeyboardMarkup(
    [["📘 آموزش", "📄 درباره"],
     ["☎️ تماس"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\nبه بات آموزشی خوش اومدی",
        reply_markup=menu
    )

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📘 آموزش":
        await update.message.reply_text("درس ۱: مقدمه بات تلگرام")

    elif text == "📄 درباره":
        await update.message.reply_text("بات آموزشی نسخه ۱")

    elif text == "☎️ تماس":
        await update.message.reply_text("📧 example@gmail.com")

    else:
        await update.message.reply_text("از منو استفاده کن 👇")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler))

app.run_polling()
