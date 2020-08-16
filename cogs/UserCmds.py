import discord
import datetime
from discord.ext import commands
from discord.utils import get

NUM = 51
COLOR = 0xe10505

class User(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def pfp(self, ctx, message):

        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                embed=discord.Embed(title="Sample Profile Viewer", description=f"Gets profile of user", color=COLOR, timestamp=datetime.datetime.utcnow())
                embed.set_author(name="Sample Bot")
                embed.set_image(url=(user.avatar_url))
                embed.set_footer(text="<YOUR USERNAME>")
                await ctx.send(embed=embed)
        else:
            await ctx.send("Sample Bot -> No user given")


    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

def setup(bot):
    bot.add_cog(User(bot))