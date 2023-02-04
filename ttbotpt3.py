import discord
from discord.ext import commands 
import asyncio 

client = commands.Bot(help_command = None, command_prefix='*', intents=discord.Intents.all())

print(f"Logged in as {client.user}")

@client.event
async def on_ready():
    async def change_status():
        while True:
            activity = discord.Game(name="Status 1")
            await client.change_presence(activity=activity)
            await asyncio.sleep(30)
            activity = discord.Game(name="Status 2")
            await client.change_presence(activity=activity)
            await asyncio.sleep(30)
    client.loop.create_task(change_status())

@client.command()
async def test(ctx):
  await ctx.send("Hello, World!")

@client.command()
async def clear(ctx, num_messages: int):
  channel = ctx.message.channel
  if isinstance(channel, discord.TextChannel):
    await channel.purge(limit=num_messages +1)


client.run("TOKEN_HERE")
