import discord
import os
from keep_alive import keep_alive

client = discord.Client()
MINT_SIZE = 2500

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

"""

An async function that fetchs doggo image by id number.

"""
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        # Get the id number after !
        Id = message.content[1:]
        # Remove leading zeros except for one zero
        Id = Id.lstrip("0") or "0"
        # Error checking the id number
        if Id.isdigit() and 0 <= int(Id) < MINT_SIZE:
            img_url = f"https://vaxxeddoggos.com/assets/doggos/{Id}.png"
            embed = discord.Embed( 
                title=f"Doggo #{Id}",
                color=0xb48ccb, 
                url="https://vaxxeddoggos.com/gallery"
            )
            embed.set_image(url=img_url)
            await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))
