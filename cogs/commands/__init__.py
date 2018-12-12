import discord
from discord.ext import commands


class Commands:
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.get_emotions())

    async def get_emotions(self):
        async with self.bot.session.get("https://goodani.me/api/v1/emotions") as r:
            j = await r.json()
        self.bot.emotions = list(j.keys())

    @commands.command(aliases=["picture", "pic", "gif"])
    async def emotion(self, ctx, *, emotion: str.lower):
        """Sends an emotion picture if found."""
        if not emotion in self.bot.emotions:  # we do not have this emotion available
            return await ctx.send("Emotion does not exist!")
        async with self.bot.session.get(
            f"https://goodani.me/api/v1/emotion/{emotion}"
        ) as r:
            j = await r.json()
        if j["is_nsfw"] and not ctx.channel.is_nsfw():
            return await ctx.send("NSFW emotion!")
        em = discord.Embed(title=emotion, colour=0xAD004B)
        em.set_image(url=j["url"])
        await ctx.send(embed=em)

    # some predefined commands

    @commands.command()
    async def hug(self, ctx, *, user: discord.User):
        """Hug someone."""
        async with self.bot.session.get(f"https://goodani.me/api/v1/emotion/hug") as r:
            j = await r.json()
        em = discord.Embed(
            title="Hug!",
            description=f"{ctx.author.mention} hugged {user.mention}! How cute!",
            colour=0xAD004B,
        )
        em.set_image(url=j["url"])
        await ctx.send(embed=em)

    @commands.command()
    async def kiss(self, ctx, *, user: discord.User):
        """Kiss someone."""
        async with self.bot.session.get(
            f"https://goodani.me/api/v1/emotion/kiss"
        ) as r:
            j = await r.json()
        em = discord.Embed(
            title="Kiss!",
            description=f"{ctx.author.mention} kissed {user.mention}! True love?",
            colour=0xAD004B,
        )
        em.set_image(url=j["url"])
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Commands(bot))
