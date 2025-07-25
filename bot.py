from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
import logging

# إعدادات التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEB_APP_URL = "https://premarket.neocities.org"  # رابط موقعك

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # زر لفتح الميني أب + زر للعودة إلى البوت
    keyboard = [
        [InlineKeyboardButton("فتح المتجر 🛒", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton("الذهاب إلى البوت ↩️", url="https://t.me/giftspremarketbot")]
    ]
    
    await update.message.reply_text(
        "مرحباً في متجر الهدايا!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # استقبال بيانات من الميني أب
    data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"تم استلام الطلب: {data}")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    
    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    
    app.run_polling()