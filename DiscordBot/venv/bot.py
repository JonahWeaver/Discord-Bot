import asyncio
import discord
import requests
import yt_dlp
import responses
import piechart
import count
import logging
from discord.ext import commands

import musicutilities

import os
os.environ['PATH'] = os.environ['PATH'] + ';C:\\Users\\Emily Rose\\Desktop\\ffmpeg-master-latest-win64-gpl\\bin'

filePath = 'C:/Users/Emily Rose/source/repos/DiscordBotData/'
piePath = 'C:/Users/Emily Rose/source/repos/DiscordBot/'

async def send_message(message, user_message, is_private):
    try:
        response= responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    file1 = open(filePath+ 'JobotID.txt', 'r')
    file2 = open(filePath+ 'ChannelID.txt', 'r')

    TOKEN= str(file1.readline())
    countChannelID = int(file2.readline())
    intents=discord.Intents.default()
    intents.message_content=True
    intents.members = True
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix='!', intents=intents)

    @client.event
    async def on_ready():
        his = await get_result(countChannelID)
        count.retrieve_messages(his)
        piechart.makechart(count.numList, count.userList, piePath)
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.channel.id == countChannelID:
            count.addCount(message)
            piechart.makechart(count.numList, count.userList, piePath)
        if message.content.startswith('!play'):
            query = message.content[6:]
            ydl_opts = {
                'default_search': 'ytsearch',
                'format': 'bestaudio/best',
                'noplaylist': True,
                'quiet': True,
                'no_warnings': True,
                'process' : False
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                search_results = ydl.extract_info(query, download=False)['entries']
                url = search_results[0]['url']

            voice_channel = message.author.voice.channel
            voice_client = await voice_channel.connect()
            source = discord.FFmpegPCMAudio(url)
            voice_client.play(source)
        else:
            username= str(message.author)
            user_message= str(message.content)
            channel= str(message.channel)

            print(f"{username} said: '{user_message}' ({channel})")

            if len(user_message)==0:
                t=1#do nothing
            elif(user_message[0]=='?'):
                user_message=user_message[1:]
                await send_message(message, user_message, is_private=True)
            elif (user_message== '!chart'):
                with open(piePath + 'countingPie.png', 'rb') as f:
                    picture = discord.File(f)
                    await message.channel.send(file=picture)
            else:
                await send_message(message, user_message, is_private=False)

    async def get_result(id):
        l = []
        channelName = client.get_channel(id)
        async for i in channelName.history(oldest_first=True, limit= 100000):
            l.append(i)
        return l

    client.run(TOKEN)