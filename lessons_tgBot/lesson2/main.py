from datetime import *

import aiogram.utils.exceptions
from aiogram import Bot, Dispatcher, executor, types
from config import *

bot = Bot(TOKEN_tgAPI)
dp = Dispatcher(bot)

helpCommands = """
/start - start
/help - help"""
callCount = 0


async def on_startup(_):
    print("Start execution 0")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=helpCommands)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<b>welcome</b>', parse_mode="HTML")
    await message.answer('user id is ' + str(message.from_user.id))
    print("id = " + str(bot.id))
    # await message.delete()


@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global callCount
    await message.answer(text='..in /count')
    await message.answer(text=f'count = {callCount}')
    callCount += 1


chatID = "-1001190770776"   # looking for chat_id
                            # for private channel web.telegram.org/z/#-XXXXXXXXX chat_id = -100XXXXXXXXX
                            # for public channel web.telegram.org/name chat_id = name


@dp.message_handler(commands=['give'])
async def give_command(message: chatID):
    try:
        await bot.send_message(chat_id=chatID, text='send text')
    except aiogram.utils.exceptions.ChatNotFound:
        await message.answer(text=f'ChatNotFound {chatID}')


userID = 299599327
now = datetime.now().strftime("%d-%m-%Y %H:%M")


@dp.message_handler(commands=['sentMSG'])
async def sentMSG_command(message: userID):
    try:
        await bot.send_message(chat_id=userID, text='send text2 ' + str(now))
    except aiogram.utils.exceptions.ChatNotFound:
        await message.answer(text=f'UserNotFound {userID}')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
