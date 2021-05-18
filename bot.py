from model import *
import os
import discord
#from scoretable import scoreboard
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
image_types = ["png", "jpeg", "gif", "jpg"]
TOKEN =""
GUILD="testing"
from discord.ext import commands

#bot = commands.Bot(command_prefix='$')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        #print(f'{guild} has connected the bot')
        #print(guild.members)
        if guild.name == GUILD:
            print("Bonjour")
            break

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            await attachment.save("sample.png")
            filter_func("sample.png")
            #display toonify
            await message.channel.send(file=discord.File("toonify.jpg"))
            await message.channel.send(file=discord.File("blackwhite.jpg"))
    if message.content.startswith('>help'):
        message2='This bot is currently in development, '+str(message.author)[:-5]+'.The commands availabe are >hi , >click a pic'
        await message.channel.send('{}'.format(message2))
    
    

'''@bot.command()
async def test(ctx, arg):
     ctx.send(arg)
'''

    

client.run(TOKEN)
