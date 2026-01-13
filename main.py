import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🤖 Oxide bot запущен!\n"
        "Команды:\n"
        "/dice — бросить кость\n"
        "/nick — привязать ник"
    )


@dp.message(Command("dice"))
async def dice(message: Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("nick"))
async def set_nick(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("❌ Использование: /nick ТВОЙ_НИК")
        return

    nick = args[1]
    await message.answer(f"✅ Ник сохранён: <b>{nick}</b>", parse_mode="HTML")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
