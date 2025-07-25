from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging
import asyncio

# إعدادات التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("❌ ERROR: BOT_TOKEN is not set!")
    exit(1)

WEB_APP_URL = "https://premarket.neocities.org"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [[InlineKeyboardButton("🎁 Open Gift Market", web_app=WebAppInfo(url=WEB_APP_URL))]]
        await update.message.reply_text(
            "🚀 Welcome to Gift Market Bot!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    except Exception as e:
        logger.error(f"Error: {e}")

async def main():
    try:
        logger.info("Starting bot...")
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        await app.run_polling()
    except Exception as e:
        logger.error(f"Bot failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())