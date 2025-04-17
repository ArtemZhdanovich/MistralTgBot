import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from tg_bot.mistral import mistral_get_content
from tg_bot.semantic import semantic_analyze

from sentence_transformers import SentenceTransformer

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

model = SentenceTransformer("all-MiniLM-L6-v2")
sentences = [
    "Какой сегодня день",
    "Какой сегодня год",
    "Почему небо синее",
]

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        content = semantic_analyze(model, sentences, message.text)
        answer = await mistral_get_content(content)
        await message.answer(answer)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())