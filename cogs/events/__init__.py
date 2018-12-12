import discord
import sys
import traceback
from discord.ext import commands


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, msg):
        if msg.author.bot:
            return

    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)
        if isinstance(error, discord.Forbidden):
            return
        elif isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.NotOwner):
            return await ctx.send("No u")
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr
        )

    async def on_ready(self):
        print("Ready")


def setup(bot):
    bot.add_cog(Events(bot))
