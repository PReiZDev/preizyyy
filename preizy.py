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

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="diep.io"))
#----------------------Stats-----------------------
@bot.listen()
async def on_member_join(member):
    botserver = bot.get_server(id="411833498207256576")
    membersroom = bot.get_channel(id="460456526449082378")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")

@bot.listen()
async def on_member_remove(member):
    botserver = bot.get_server(id="411833498207256576")
    membersroom = bot.get_channel(id="460456526449082378")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")

@bot.event
async def on_server_role_create(role):
    botserver = bot.get_server(id="411833498207256576")
    rolesroom = bot.get_channel(id="460456598473670696")
    await bot.edit_channel(rolesroom, name=f"🔴Roles: {len(botserver.roles)}")  

@bot.event
async def on_server_role_delete(role):
    botserver = bot.get_server(id="411833498207256576")
    rolesroom = bot.get_channel(id="460456598473670696")
    await bot.edit_channel(rolesroom, name=f"🔴Roles: {len(botserver.roles)}")  

@bot.event
async def on_channel_create(channel):
    botserver = bot.get_server(id="411833498207256576")
    channelsroom = bot.get_channel(id="460456375999266826")
    await bot.edit_channel(channelsroom, name=f"🔵Channels: {len(botserver.channels)}")

@bot.event
async def on_channel_delete(channel):
    botserver = bot.get_server(id="411833498207256576")
    channelsroom = bot.get_channel(id="460456375999266826")
    await bot.edit_channel(channelsroom, name=f"🔵Channels: {len(botserver.channels)}")

#--------------------Moderation--------------------
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user : discord.User=None, Day : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `>>ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `>>ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    elif Day is None:
        await bot.reply("**The usage is `>>ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.ban(user, delete_message_days=Day)
            LogRoom = bot.get_channel(id="412146516246003723")
            await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="BAN", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {server}`\nBAMM!! You got banned!**")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `>>kick {member} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `>>kick {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            await bot.kick(user)
            LogRoom = bot.get_channel(id="412146516246003723")
            await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="KICK", description=None, colour=0xe74c3c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {server}`\nHey! You got kicked, bai bai!**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User=None, duration : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is '>>mute {member} {duration(in sec)} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `>>mute {member} {duration(in sec)} {Reason}`**")
    elif duration is None:
        await bot.reply("**The usage is `>>mute {member} {duration(in sec)} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="412146516246003723")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.add_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="MUTE", description=None, colour=0x11806a)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.add_field(name="Duration", value=f"{duration} sec")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {PRserver}`\nRoses are red, violets are blue and {user.mention} is muted!**")
            await asyncio.sleep(duration)
            await bot.remove_roles(user, MutedRole)
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value="Time is up...")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {server}`\nHey! You got unmuted, dont get too excited..**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `>>unmute {member} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `>>unmute {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="412146516246003723")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.remove_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {server}`\nHey! You got unmuted, dont get too excited..**")
        
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int=None):
    if number is None:
        await bot.reply("**The usage is `>>clear {number of messages to delete}`**")
    else:
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
async def lock(ctx, duration : int=None, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `>>lock {duration (in sec)} {Reason}`**")
    elif duration is None:
        await bot.reply("**The usage is `>>lock {duration (in sec)} {Reason}`**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Member")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now locked for __{Reason}__**")
        LogRoom = bot.get_channel(id="412146516246003723")
        em = discord.Embed(title="LOCK", description=None, colour=0x1f8b4c)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.add_field(name="Duration", value=f"{duration} sec")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
        await asyncio.sleep(duration)
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="412146516246003723")
        em = discord.Embed(title="UNLOCK", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, *, Reason=None):
    if Reason is None:
        await bot.reply("**The usage is `>>unlock {Reason}`**")
    else:
        Registered = discord.utils.get(ctx.message.server.roles, name="Member")
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        await bot.edit_channel_permissions(ctx.message.channel, Registered, overwrite)
        await bot.send_message(ctx.message.channel, f"**{ctx.message.channel.mention} is now unlocked for __{Reason}__**")
        LogRoom = bot.get_channel(id="412146516246003723")
        em = discord.Embed(title="UNLOCK", description=None, colour=0x2ecc71)
        em.add_field(name="Channel", value=f"{ctx.message.channel.mention}")
        em.add_field(name="Moderator", value=f"{ctx.message.author}")
        em.add_field(name="Reason", value=f"{Reason}")
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        em.set_footer(text=timer)
        await bot.send_message(LogRoom, embed=em)
    
#--------------------------------------------------
@bot.command(pass_context=True)
async def shift(ctx):
    words = ["chicken", "no u", "what?", "u wot", "hippo", "crab", "teddy", "Rettend", "PReiZy", "PReiZ", "javascript", "diep.io", "update"]
    word = random.choice(words)
    text = list(word)
    text = random.shuffle(text)
    text = str(text)
    e = discord.Embed(title="", description=f"*{text}*", colour=0x607d8b)
    await bot.say("**Try yourself!\nGet Ready!**")
    asyncio.sleep(2)
    await bot.say(embed=e)
    await bot.wait_for_message(author=ctx.message.author, content=text)
    await bot.send_message(ctx.message.channel, f"**The word was {word}**")

@bot.command(pass_context=True)
async def tag(ctx):
    await bot.say("**[ρπ]**")

@bot.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description=":ping_pong: **...**", colour=0x3498db)
    msg = await bot.say(embed=embed)
    ping = (time.monotonic() - before) * 1000
    pinges = int(ping)
    if 999 > pinges > 400:
        mesg = "Thats a lot!"
    elif pinges > 1000:
        mesg = "Omg, really sloooooow...."
    elif 399 > pinges > 141:
        mesg = "Ahhh, not good!"
    elif pinges < 140:
        mesg = "Its Good, Boi ;)"
    em = discord.Embed(title=None, description=f":ping_pong: Seems like `{pinges}` MS\n{mesg}", colour=0x3498db)
    em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    em.set_footer(text=timer)
    await bot.edit_message(msg, embed=em)

@bot.command(pass_context=True)
async def say(ctx, *, words):
    await bot.say(f"**{words}**")
    
@bot.command(pass_context=True)
async def roll(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `>>roll {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `>>roll {number} {number}`**")
    else:
        msg = random.randint(x, y)
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**My choose: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `>>sub {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `>>sub {number} {number}`**")
    else:
        msg = x - y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `>>mul {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `>>mul {number} {number}`**")
    else:
        msg = x * y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `>>div {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `>>div {number} {number}`**")
    else:
        msg = x / y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `>>exp {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `>>exp {number} {number}`**")
    else:
        msg = x ** y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `>>add {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `>>add {number} {number}`**")
    else:
        msg = x + y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command()
async def game(*, play=None):
    if play is None:
        await bot.reply("**The usage is `>>game {Something to set as a game}`**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await bot.reply("**The usage is `>>name {Something to set as your name}`**")
    else:
        await bot.change_nickname(ctx.message.author, name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x3498db)
        await bot.say(embed=em)
    
@bot.command(pass_context=True)
async def suggest(ctx, pref=None, *, text=None):
    if pref is None:
        await bot.reply("**The usage is `>>suggest {prefix (Q, S, C, B)} {text}`**")
    elif text is None:
        await bot.reply("**The usage is `>>suggest {prefix (Q, S, C, B)} {text}`**")
    else:
        try:
            if pref is "S":
                msg = "SUGGESTION"
            if pref is "Q":
                msg = "QUESTION"
            if pref is "C":
                msg = "COMMAND SUGGESTION"
            if pref is "B":
                msg = "BUGS"
            else:
                bot.say("**Please use a valid prefix! The available prefixes: __Q__, __S__, __C__, __B__**")
        finally:
            colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
            col = random.choice(colours)
            em = discord.Embed(title=f"{msg}", description=f"**From {ctx.message.author.mention}**\n⋙ {text}", colour=col)
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            channel = bot.get_channel(id="426733808205692928")
            await bot.send_message(ctx.message.channel, f"**:white_check_mark: Sent in {channel.mention}**")
            mesg = await bot.send_message(channel, embed=em)
            if pref is "S":
                await bot.add_reaction(mesg, "👍")
                await bot.add_reaction(mesg, "👎")
            if pref is "C":
                await bot.add_reaction(mesg, "👍")
                await bot.add_reaction(mesg, "👎")
            
@bot.command(pass_context=True)
async def poll(ctx, options: str=None, *, question=None):
    if options is None:
        await bot.reply("**The usage is `>>poll {options (2-10)} {Question or Suggestion}`**")
    elif question is None:
        await bot.reply("**The usage is `>>poll {options (2-10)} {Question or Suggestion}`**")
    else:
        if len(options) <= 1:
            await bot.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await bot.say('You cannot make a poll for more than 10 things!')
            return
        if len(options) == 2:
            reactions = ['👍', '👎']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description), colour=0x3498db)
        react_message = await bot.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await bot.add_reaction(react_message, reaction)
        await bot.edit_message(react_message, embed=embed)

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
                     ":notepad_spiral: The Unban command doesn't works, sorry about that. You need to unban the user from `Server Settings->Bans`\n"
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
                      ":notepad_spiral: >>help\n"
                      "\n"
                      ":notepad_spiral: >>tag\n"
                      "\n"
                      ":notepad_spiral: >>nick {name}\n"
                      ":bulb: Set your nickname\n"
                      "\n"
                      ":notepad_spiral: >>time\n"
                      ":bulb: Returns the real time in UTC+0!\n"
                      "\n"
                      ":notepad_spiral: >>game {game}\n"
                      ":bulb: Set a game for the Bot\n"
                      "\n"
                      ":notepad_spiral: >>mod\n"
                      ":bulb: The Moderation commands\n"
                      "\n"
                      ":notepad_spiral: >>8ball\n"
                      ":bulb: Get answer (or not :>  ) to your question", inline=True)
        emb.set_thumbnail(url="https://cdn.discordapp.com/avatars/450246060456148993/b9fc7c3ec4dc905cc575ab313a7dba0c.webp?size=2048")
        emb.set_footer(text='------------------------')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT






token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
