import discord
import asyncio
import aiohttp
from discord.ext import commands

import config

bot = commands.Bot(command_prefix=["owo ", "aww "], case_insensitive=True)
bot.config = config


async def start_bot():
    for ext in config.exts:
        bot.load_extension(ext)
    bot.load_extension("jishaku")
    bot.session = aiohttp.ClientSession(loop=loop)
    await bot.start(config.token)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
