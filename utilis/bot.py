import asyncio
import os
from collections.abc import Awaitable
from multiprocessing.connection import answer_challenge
from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from pyexpat.errors import messages
from states import Survey
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from dotenv import load_dotenv

from keyboards import reply_kb, inline_kb

load_dotenv()

bot_token=os.getenv("TOKEN")

bot = Bot(token=bot_token)

router =  Router()


@router.message(CommandStart())
async def cmd_welcome(message: Message):
    await message.answer(f"Hello {message.from_user.first_name}!")


@router.message(Command(commands="help"))
async def cdm_help(message: Message):
    await message.answer("выбкрите опцию ")


@router.message(Command(commands="inet")
async def cdm_survey(message: Message):
    await message.answer("Вот ссылки", reply_markup=inline_kb)


@router.message(Command(commands="survey"))
async def cmd_survey(massage: Message, state: FSMContext):
    await state.update_data(name=messages.text)
    await messages.answer("как вас зовут?")
    await  state.set_state(Survey.name)

@router.message(Survey.name, F.text)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name= ())


@router.message(Survey.age, F.text)
async def process_name(message: Message, state: FSMContext):
    await message.reply(name=message.text)
    await message.answer('Какщй ваш любимый цвет ?')
    await state.set_state(Survey.color)


@router.message(F.text)
async def reply_text(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    age = data.get('age')
    color = message.text
    answer_text = f'''
                    отлично !!!\n Спасибо за пройденный опрос!!!
                    Ваш любимый цвет {color}\n вам {age} лет\nвас зовут{name}'''
    await  message.answer(answer_text)
    await state.clear()


@router.message(F.text)
async def reply_text(message: Message):
    if message =="hi":
        await message.reply('и тебе привет')
    else:
       await message.reply(f"You typed {message.text}")


@router.message(F.photo)
async def reply_image(message: Message):
    await message.reply(f"Nice picture {message.text}")



async def main():
    print("Starting bot...")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())