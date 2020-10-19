import random
import discord
import asyncio
from discord.ext import commands
prefix = "!fb "
bot = commands.Bot(command_prefix = "!fb ")
token = 'NzY2NDM1NDUzNzAzNTUzMDk0.X4jUow.8Jw9lX8uktVaXHYvi_IzLfeYyBs'
@bot.event
async def on_ready():
	print("The bot is ready.")

@bot.command(pass_context = True)
async def randomnumber(ctx):
	embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0xF85252))
	await ctx.send(embed = embed)

bot.run(token)
