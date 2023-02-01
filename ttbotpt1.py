import discord
from discord.ext import commands 
 
client = commands.Bot(help_command = None, command_prefix='*', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in")
    
@client.command()
async def test(ctx):
  await ctx.send("Hello, World!")
  
  
client.run(TOKEN_HERE)
