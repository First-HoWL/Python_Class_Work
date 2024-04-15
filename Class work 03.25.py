#https://mastergroosha.github.io/aiogram-3-guide/quickstart/
import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token="7161846829:AAEcozQpBztwMJ0ntcypIAD3oNHkiIH6s4w")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Pinus!")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("/help - отримати довідку за командами\n/start - почати СПАМ\n/roll - рандомне число від 1 до 100")

    #await bot.send_message(chat_id= message.chat.id, text='Help message')
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    for i in range(100):
        await message.answer("Sosi jopy!")


@dp.message(Command("roll"))
async def cmd_roll(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        await message.answer(f"Випадкове число від 1 до {args[0]}: {random.randint(1, int(args[0]))}") 
    else:
        await message.answer(f"Випадкове число від 1 до 100: {random.randint(1, 100)}")

# @dp.message()
# async def message(message: types.Message):
#     await message.answer(message.text)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


