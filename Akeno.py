import asyncio
import discord
import requests

intents = discord.Intents.default()
intents.guild_messages = True
client = discord.Client(intents=intents)

async def send_waifu():
    while True:
        response1 = requests.get('https://api.waifu.pics/sfw/waifu')
        response2 = requests.get('https://api.waifu.pics/nsfw/waifu')
        img_url1 = response1.json()['url']
        img_url2 = response2.json()['url']


        waifu_chan = client.get_channel(ur channel id)
        ecchi_chan = client.get_channel(ur channel id)

        await waifu_chan.send("TESTING!!!")
        await waifu_chan.send(img_url2)

        await asyncio.sleep(1)

async def on_ready():
        print("Ready!")
        await client.change_presence(activity=discord.Game(name='Watching Anime'))
        client.loop.create_task(send_waifu())

client.run("BOT_TOKEN HERE!!!")
    
