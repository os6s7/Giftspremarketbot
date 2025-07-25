‏from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
‏from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
‏import os
‏import logging
‏import asyncio

# إعدادات متقدمة للتسجيل
‏logging.basicConfig(
‏    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
‏    level=logging.INFO
)
‏logger = logging.getLogger(__name__)

‏BOT_TOKEN = os.getenv("BOT_TOKEN")
‏if not BOT_TOKEN:
‏    logger.error("❌ BOT_TOKEN غير موجود!")
‏    exit(1)

‏WEB_APP_URL = "https://premarket.neocities.org"

‏async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
‏    try:
‏        keyboard = [[InlineKeyboardButton("🎁 Open Gift Market", web_app=WebAppInfo(url=WEB_APP_URL))]]
‏        await update.message.reply_text(
            "مرحباً! اضغط أدناه لفتح التطبيق 👇",
‏            reply_markup=InlineKeyboardMarkup(keyboard))
‏    except Exception as e:
‏        logger.error(f"خطأ في الأمر start: {e}")

‏async def run_bot():
‏    app = ApplicationBuilder().token(BOT_TOKEN).build()
‏    app.add_handler(CommandHandler("start", start))
‏    await app.run_polling()

‏if __name__ == "__main__":
    # إضافة هذه السطور للتعامل مع المنفذ المطلوب
‏    port = int(os.environ.get('PORT', 5000))
‏    logger.info(f"Using port: {port}")
    
‏    try:
‏        asyncio.run(run_bot())
‏    except KeyboardInterrupt:
‏        logger.info("إيقاف البوت...")
‏    except Exception as e:
‏        logger.error(f"خطأ غير متوقع: {e}")
‏        from fastapi import FastAPI
‏import uvicorn

‏app = FastAPI()

‏@app.get("/")
‏def home():
‏    return {"status": "Bot is running"}

‏if __name__ == "__main__":
‏    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))