import discord
import datetime
from discord.ext import commands

COLOR = 0xe10505

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help Page", description="Page (1/1)", color=COLOR, timestamp=datetime.datetime.utcnow())    
        embed.set_author(name="Sample Bot")
        embed.add_field(name="$help", value="Displays this page", inline=False)
        embed.add_field(name="$eightball <question>", value="Tells your fortune", inline=False)
        embed.add_field(name="$ping", value="checks if bot is online", inline=False)
        embed.add_field(name="$roll <num1> <num2>", value="rolls a number between num1 and num2", inline=False)
        embed.add_field(name="$coinflip", value="flips a coin", inline=False)
        embed.set_footer(text="<YOUR USERNAME>")
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed=discord.Embed(title="Info Page", color=COLOR, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Sample Bot")
        embed.add_field(name="Language", value="Python 3.8", inline=True)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.set_footer(text="<YOUR USERNAME>")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))