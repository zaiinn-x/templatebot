import discord
import os
from discord.ext import commands


TOKEN = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN' # replace with token


client = commands.Bot(command_prefix="$")
client.remove_command("help")

def cogloader():
    for files in os.listdir("./cogs"):
        if files.endswith(".py"):
            client.load_extension(f"cogs.{files[:-3]}")
            print("Cog loaded -> " + str(files))

@client.event
async def on_ready():
    
    cogloader()

    print("\nLogged in\n")
    print("Username: " + str(client.user.name))
    print("ID: " + str(client.user.id) + "\n")

    
client.run(TOKEN)
