import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from time import gmtime
from discord.ext import commands

bot = commands.Bot(command_prefix='>>', description=None)
message = discord.Message
server = discord.Server
member = discord.Member
user = discord.User
permissions = discord.Permissions
"""
Write this when you need the command's triggered time in UTC

timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())"""

bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="diep.io"))

@bot.command(pass_context=True)
async def roll(ctx, x : int, y : int):
    msg = random.randint(x, y)
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**My choose: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int, y : int):
    msg = x - y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**Tthe result: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int, y : int):
    msg = x * y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int, y : int):
    msg = x / y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int, y : int):
    msg = x ** y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int, y : int):
    msg = x + y
    text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
    await asyncio.sleep(3)
    await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command()
async def game(play):
    await bot.change_presence(game=discord.Game(name=play))
    em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x95a5a6)
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def time(ctx):
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    await bot.say(f"**{ctx.message.author.mention}, the time is __{timer}__**")

@bot.command(pass_context=True)
async def nick(ctx, name):
    await bot.change_nickname(ctx.message.author, name)
    em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x95a5a6)
    await bot.say(embed=em)

@bot.event
async def on_message(message):
    if message.content.startswith(">>commands"):
        emb = discord.Embed(title="COMMANDS", description="Check my commands!", colour=0x95a5a6)
        emb.add_field(name='------------------------', value=":notepad_spiral:  >>commands\n"
                      "Shows this message\n"
                      "\n"
                      ":notepad_spiral: >>add {number} {number}\n"
                      ":notepad_spiral: >>sub {number} {number}\n"
                      ":notepad_spiral: >>mul {number} {number}\n"
                      ":notepad_spiral: >>div {number} {number}\n"
                      "\n"
                      ":notepad_spiral: >>roll {number} {number}\n"
                      "Choose between two numbers\n"
                      "\n"
                      ":notepad_spiral: >>nick {name}\n"
                      "Set your nickname\n"
                      "\n"
                      ":notepad_spiral: >>time\n"
                      "Returns the real time in UTC+0\n"
                      "\n"
                      ":notepad_spiral: >>game {game}\n"
                      "Set a game for the Bot", inline=True)
        emb.set_thumbnail(url="https://cdn.discordapp.com/avatars/450246060456148993/b9fc7c3ec4dc905cc575ab313a7dba0c.webp?size=2048")
        emb.set_footer(text='------------------------')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT






token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
