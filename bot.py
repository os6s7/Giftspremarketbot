from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

WEB_APP_URL = os.getenv("WEB_APP_URL", "https://your-web-app.onrender.com")

def main():
    # Create application
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    
    # Add command handler
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        button = InlineKeyboardButton(
            "Open Web App",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
        await update.message.reply_text(
            "Click below to launch:",
            reply_markup=InlineKeyboardMarkup([[button]])
        )
    
    application.add_handler(CommandHandler("start", start))
    
    # Run application
    application.run_polling()

if __name__ == "__main__":
    main()