import asyncio
import discord
from datetime import datetime
import os

token = os.getenv('DISCORD_CONTROL_BOT')
author_id = int(os.getenv('DISCORD_AUTHOR_ID'))
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    pass
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == author_id:
        if message.guild is None:
            command = str(message.content)
            if command == " " or command == "" or command == None:
                sent_message = await message.channel.send('Jabājabā wa arimasen, baka...', reference=message)
                await asyncio.sleep(5)
                await sent_message.delete()
                await message.delete()
            if command.lower().replace(" ", "") == "start":
                os.system("code tunnel service install")
                sent_message = await message.channel.send('Service started', reference=message)
            elif command.lower().replace(" ", "") == "stop":
                os.system("code tunnel service uninstall")
                await message.channel.send('Service stopped', reference=message)
            elif command.lower().replace(" ", "") == "restart":
                os.system("code tunnel service uninstall")
                os.system("code tunnel service install")
                await message.channel.send('Service restarted', reference=message)
            else:
                await message.channel.send("nani?", reference=message)
                await asyncio.sleep(5)
                await sent_message.delete()
                await message.delete()
client.run(token=token)