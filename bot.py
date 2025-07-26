from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="افتح الميني اب 🎁",
        web_app=types.WebAppInfo(url="https://telegram-web-app-j6du.onrender.com/")
    ))
    await message.answer("اهلاً بك! جرّب الميني اب من الزر:", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
