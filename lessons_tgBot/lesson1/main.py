from aiogram import Bot, Dispatcher, executor, types
from config import *


bot = Bot(TOKEN_tgAPI)
dp = Dispatcher(bot)

@dp.message_handler()
async  def echo(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text=message.text.upper() + ' test')


if __name__ == '__main__':
    executor.start_polling(dp)