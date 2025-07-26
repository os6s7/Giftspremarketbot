import os
import threading
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🧠 بوت تليگرام
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ✅ رسالة start مع زر ميني أب
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="🎁 افتح الميني أب",
        web_app=types.WebAppInfo(url="https://your-mini-app.onrender.com")  # 🔁 عدل هذا الرابط لرابط الواجهة مالتك
    ))
    await message.answer("أهلاً بك! اضغط الزر لتجربة الميني أب:", reply_markup=keyboard)

# 🚀 بدء البوت عبر polling
def run_bot():
    executor.start_polling(dp, skip_updates=True)

# 🌐 سيرفر ويب بسيط فقط حتى ما يطلع 404 في Render
app = Flask(__name__)

@app.route('/')
def index():
    return "🤖 البوت يعمل حالياً بنجاح على Render!"

# 📦 تشغيل Flask + Aiogram بنفس الوقت
if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))