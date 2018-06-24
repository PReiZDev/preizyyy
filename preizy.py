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

#--------------------Moderation--------------------
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User, Day : int, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        room = ctx.message.channel
        await bot.ban(user, delete_message_days=Day)
        LogRoom = bot.get_channel(id="412146516246003723")
        await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xad1457)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/388945761611808769/453211671935057920/banned.gif")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user : discord.User, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        banneds = await bot.get_bans(ctx.message.server)
        if user not in banneds:
            bot.say("**Plz mention a banned user!**")
        else:
            room = ctx.message.channel
            await bot.unban(ctx.message.server, user)
            LogRoom = bot.get_channel(id="412146516246003723")
            await bot.say(f"**{user.mention} got unbanned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓑𝓐𝓝⧸⎠╱", description=None, colour=0xe91e63)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        room = ctx.message.channel
        await bot.kick(user)
        LogRoom = bot.get_channel(id="412146516246003723")
        await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓚𝓘𝓒𝓚⧸⎠╱", description=None, colour=0xe74c3c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User, duration : int, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        LogRoom = bot.get_channel(id="412146516246003723")
        room = ctx.message.channel
        MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.add_roles(user, MutedRole)
        await bot.say(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x11806a)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        await bot.remove_roles(user, MutedRole)
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value="Time is up...")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User, Reason):
    if user.id == ctx.message.author.id:
        await bot.say("**I won't let you moderate yourself xD**")
    else:
        LogRoom = bot.get_channel(id="412146516246003723")
        room = ctx.message.channel
        MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
        await bot.remove_roles(user, MutedRole)
        await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
        em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓜𝓤𝓣𝓔⧸⎠╱", description=None, colour=0x1abc9c)
        em.add_field(name="User", value=f"{user.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int):
    number += 1
    deleted = await bot.purge_from(ctx.message.channel, limit=number)
    num = number - 1
    LogRoom = bot.get_channel(id="412146516246003723")
    em = discord.Embed(title=None, description=f'{ctx.message.author} deleted __{num}__ messages', colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    msg = await bot.send_message(ctx.message.channel, embed=em)
    await bot.send_message(LogRoom, embed=em)
    await asyncio.sleep(4)
    await bot.delete_message(msg)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, Reason):
    Registered = discord.utils.get(ctx.message.server.roles, name="Member")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
    await bot.send_message(room, f"**{ctx.message.channel.mention} is now locked!**")
    LogRoom = bot.get_channel(id="412146516246003723")
    em = discord.Embed(title="╲⎝⧹𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x1f8b4c)
    em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
    em.add_field(name="Moderator", value=f"{ctx.message.author}")
    em.add_field(name="Reason", value=f"{Reason}")
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    Registered = discord.utils.get(ctx.message.server.roles, name="Member")
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
    await bot.send_message(room, f"**{ctx.message.channel.mention} is now unlocked, feel free to chat!**")
    LogRoom = bot.get_channel(id="412146516246003723")
    em = discord.Embed(title="╲⎝⧹𝓤𝓝𝓛𝓞𝓒𝓚⧸⎠╱", description=None, colour=0x2ecc71)
    em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
    em.add_field(name="Moderator", value=f"{ctx.message.author}")
    em.add_field(name="Reason", value=f"{Reason}")
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.send_message(LogRoom, embed=em)
#---------------------------------------------------
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
async def nick(ctx, name):
    await bot.change_nickname(ctx.message.author, name)
    em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x95a5a6)
    await bot.say(embed=em)

@bot.event
async def on_message(message):
    if message.content.startswith('>>8ball'):
        await bot.send_message(message.channel, random.choice(['**It is certain :8ball:**',
                                                              '**It is decidedly so :8ball:**',
                                                              '**Without a doubt :8ball:**',
                                                              '**No U :8ball:**',
                                                              '**Boi, go sleep... :8ball:**',
                                                              '**As i see it, yes :8ball:**',
                                                              '**As i see it, *No U*   :8ball:**',
                                                              '**Most likely :8ball:**',
                                                              '**Outlook good :8ball:**',
                                                              '**Yes :8ball:**',
                                                              '**Signs point to yes :8ball:**',
                                                              '**Reply hazy try again :8ball:**',
                                                              '**Ask again later, nub :8ball:**',
                                                              '**Better not tell you :8ball:**',
                                                              '**Cannot predict now :8ball:**',
                                                              '**Concentrate and ask again :8ball:**',
                                                              '**8ball.exe not found :8ball:**',
                                                              '**Dont count on it :8ball:**',
                                                              '**My reply is no :8ball:**',
                                                              '**My sources say no :8ball:**',
                                                              '**Outloook not so good :8ball:**',
                                                              '**Very doubtful :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Ask it to ur mum :8ball:**',
                                                              '**o** :8ball:',
                                                              '**ask it to PReiZ** :8ball:',
                                                              '***REEEE* :8ball:**',]))
    if message.content.startswith(">>time"):
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        await bot.send_message(message.channel, f"**{message.author.mention}, the time is __{timer}__**")
    if message.content.startswith(">>mod"):
        em = discord.Embed(title="MODERATION COMMANDS", description=None, colour=0x3498db)
        em.add_field(name="Admin commands", value=":notepad_spiral: >>ban {member} {0 - 7 amount of days to delete his messages} \"{Reason}\"\n"
                     ":bulb: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n"
                     ":notepad_spiral: >>unban {member} \"{Reason}\"\n"
                     ":bulb: UnBans the Banned user, the user now can rejoin by instant-invite links\n\n\n")
        em.add_field(name="Mod commands", value=":notepad_spiral: >>kick {member} \"{Reason}\"\n"
                     ":bulb: Kicks the user from the server, the user can rejoin by instant-invite links\n"
                     "\n"
                     ":notepad_spiral: >>mute {member} {duration(in sec)} \"{Reason}\"\n"
                     ":bulb: Mutes the user, this user can't send messages for the given duration, if the _time is up,_ he will auto get unmuted\n"
                     "\n"
                     ":notepad_spiral: >>unmute {member} \"{Reason}\"\n"
                     ":bulb: UnMutes the Muted user, this user now allowed to send messages\n"
                     "\n"
                     ":notepad_spiral: >>lock \"{Reason}\"\n"
                     ":bulb: Locks down the currently channel, only Admins can send messages until an unlock\n"
                     "\n"
                     ":notepad_spiral: >>unlock \"{Reason}\"\n"
                     ":bulb: Unlocks the currently locked channel, now everyone can send messages there")
        await bot.send_message(message.channel, embed=em)
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
                      ":bulb: Choose between two numbers\n"
                      "\n"
                      ":notepad_spiral: >>nick {name}\n"
                      ":bulb: Set your nickname\n"
                      "\n"
                      ":notepad_spiral: >>time\n"
                      ":bulb: Returns the real time in UTC+0\n"
                      "\n"
                      ":notepad_spiral: >>game {game}\n"
                      ":bulb: Set a game for the Bot\n"
                      "\n"
                      ":notepad_spiral: >>8ball\n"
                      ":bulb: Get answer (or not :>  ) to your question", inline=True)
        emb.set_thumbnail(url="https://cdn.discordapp.com/avatars/450246060456148993/b9fc7c3ec4dc905cc575ab313a7dba0c.webp?size=2048")
        emb.set_footer(text='------------------------')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT






token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
