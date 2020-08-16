import discord
import random
import os
import subprocess
from discord.ext import commands

NUM = 51
COLOR = 0xe10505

eightballlist = ["yeah", "perhaps", "ofc", "next question",
 "idk", "nope", "no", "onto the next question", "dont get mad, get amd", "probably not", "yea but actually no", "sounds good", "try again"]


class Gamers(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def coinflip(self, ctx):
        
        num = random.randint(1,2)
        if num == 1:
            await ctx.send(":heavy_dollar_sign: - Flipping...\n:heavy_dollar_sign: - **Heads**")
        else:
            await ctx.send(":heavy_dollar_sign: - Flipping...\n:heavy_dollar_sign: - **Tails**")

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx,*,question : str=None):
        answers = random.randint(0, 12)
        

        if question is None:
            await ctx.send(":8ball: - probably wanna say something next time")
        else:
            await ctx.send(f":8ball: - {eightballlist[answers]}")
        

    @commands.command()
    async def roll(self, ctx, num1 : int=None, num2 : int=None):
        if num1 == None or num2 == None:
                await ctx.send("**ERROR** Missing required arguments!")
        else:
            num = random.randint(num1, num2)
            await ctx.send(f":game_die: - Rolling...\n:game_die: -> **{num}**")



def setup(bot):
    bot.add_cog(Gamers(bot))