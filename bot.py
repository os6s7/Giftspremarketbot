from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging
import asyncio

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WEB_APP_URL = "https://your-web-app-url.onrender.com"  # Update this with your actual URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton(
        "Open Web App",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    await update.message.reply_text(
        "Please click the button below to open the app:",
        reply_markup=InlineKeyboardMarkup([[button]])
    )

async def main():
    """Run the bot."""
    # Create the Application
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    
    # Run the bot until the user presses Ctrl-C
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())