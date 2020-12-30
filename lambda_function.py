#!/usr/bin/env python3
import asyncio
import discord
import os

client= discord.Client()
TOKEN = os.getenv('USER_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
MESSAGE = os.getenv('MESSAGE')

def lambda_handler(event, context):
    print("lambda start")
    client.run(TOKEN, bot=False)

@client.event
async def on_ready():
    print('%s has connected to Discord!' % client.user)
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(MESSAGE)
        print("message sent")
    else:
        print("channel not found")
    await client.close()
