import asyncio
import logging
from pathlib import Path

from modules import io

import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

tokenPath = Path('token.txt').resolve()

async def main():
    token = io.readfile(tokenPath)
    bot = telegram.Bot(token)
    async with bot:
        updates = (await bot.get_updates())[0]
        print(updates)


if __name__ == '__main__':
    asyncio.run(main())