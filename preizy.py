import discord, logging, json, asyncio, time, random, aiohttp, re, datetime, traceback, os, sys, math
from time import gmtime
from discord.ext import commands

bot = commands.Bot(command_prefix='-', description=None)
Delete_LogRoom = bot.get_channel(id="411836724117897218")
LogRoom = bot.get_channel(id="412146516246003723")
Join_LogRoom = bot.get_channel(id="413272273433133066")
botserver = bot.get_server(id="411833498207256576")
timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

@bot.event
async def on_ready():
    print('Let\'s GO!')
    await bot.change_presence(game=discord.Game(name="diep.io"))
    
"""# define database
conn = lite.connect("my_database.db")
cursor = conn.cursor()
# get stored object from database
sql = "SELECT * FROM my_table WHERE field_1=?"
cursor.execute(sql, [(value_1)])
data = cursor.fetchall()
# if object does not exist, create it
if len(data) == 0:
    sql = "INSERT INTO my_table VALUES (?, ?)"
    cursor.execute(sql, [(value_1), (value_2)])
# if stored object exist and we need update it
elif ...:
    sql = "UPDATE my_table SET field_2 = ? WHERE field_1 = ?"
    cursor.execute(sql, [(value_2), (value_1)])
else:
    # get data from first object
    value_of_field_1 = data[0][0]
    # get data from third object
    value_of_field_2 = data[2][1]
# close database connection
conn.commit()
conn.close()"""

#----------------------Stats-----------------------
@bot.listen()
async def on_message_delete(message):
    Delete_LogRoom = bot.get_channel(id="411836724117897218")
    e = discord.Embed(title="DELETE", description="", colour=0xe74c3c)
    e.add_field(name="User", value=f"{message.author}")
    e.add_field(name="Channel", value=f"{message.channel}")
    e.add_field(name="Message", value=f"```autohotkey\n{message.content}\n```")
    e.set_footer(text=timer)
    await bot.send_message(Delete_LogRoom, embed=e)

"""@bot.listen()
async def on_message_edit(before, after):
    Delete_LogRoom = bot.get_channel(id="411836724117897218")
    e = discord.Embed(title="EDIT", description="", colour=0xe67e22)
    e.add_field(name="User", value=f"{before.author}")
    e.add_field(name="Before", value=f"```autohotkey\n{before.content}\n```")
    e.add_field(name="After", value=f"```autohotkey\n{after.content}\n```")
    e.set_footer(text=timer)
    await bot.send_message(Delete_LogRoom, embed=e)"""

@bot.listen()
async def on_member_join(member):
    Join_LogRoom = bot.get_channel(id="413272273433133066")
    botserver = bot.get_server(id="411833498207256576")
    membersroom = bot.get_channel(id="460456526449082378")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")
    await bot.send_message(Join_LogRoom, f"**{member.name}** has joined the server")

@bot.listen()
async def on_member_remove(member):
    Join_LogRoom = bot.get_channel(id="413272273433133066")
    botserver = bot.get_server(id="411833498207256576")
    membersroom = bot.get_channel(id="460456526449082378")
    await bot.edit_channel(membersroom, name=f"👥Members: {len(botserver.members)}")
    await bot.send_message(Join_LogRoom, f"**{member.name}** has left the server")

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
        await bot.reply("**The usage is `-ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `-ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    elif Day is None:
        await bot.reply("**The usage is `-ban {member} {0 - 7 amount of days to delete his messages} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            botserver = bot.get_server(id="411833498207256576")
            await bot.ban(user, delete_message_days=Day)
            LogRoom = bot.get_channel(id="412146516246003723")
            await bot.say(f"**{user.mention} got banned by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="BAN", description=None, colour=0xad1457)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=user.name, icon_url=user.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {botserver}`\nBAMM!! You got banned!**")

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-kick {member} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `-kick {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            room = ctx.message.channel
            botserver = bot.get_server(id="411833498207256576")
            await bot.kick(user)
            LogRoom = bot.get_channel(id="412146516246003723")
            await bot.say(f"**{user.mention} got Kicked by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="KICK", description=None, colour=0xe74c3c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=user.name, icon_url=user.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {botserver}`\nHey! You got kicked, bai bai!**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def mute(ctx, user : discord.User=None, duration : int=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is '-mute {member} {duration(in sec)} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `-mute {member} {duration(in sec)} {Reason}`**")
    elif duration is None:
        await bot.reply("**The usage is `-mute {member} {duration(in sec)} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="412146516246003723")
            botserver = bot.get_server(id="411833498207256576")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.add_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got Muted (for {duration} sec) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="MUTE", description=None, colour=0x11806a)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.add_field(name="Duration", value=f"{duration} sec")
            em.set_author(name=user.name, icon_url=user.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {botserver}`\nRoses are red, violets are blue and {user.mention} is muted!**")
            await asyncio.sleep(duration)
            await bot.remove_roles(user, MutedRole)
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value="Time is up...")
            em.set_author(name=user.name, icon_url=user.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {botserver}`\nHey! You got unmuted, dont get too excited..**")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user : discord.User=None, *, Reason=None):
    if user is None:
        await bot.reply("**The usage is `-unmute {member} {Reason}`**")
    elif Reason is None:
        await bot.reply("**The usage is `-unmute {member} {Reason}`**")
    else:
        if user.id == ctx.message.author.id:
            await bot.say("**I won't let you moderate yourself xD**")
        else:
            LogRoom = bot.get_channel(id="412146516246003723")
            botserver = bot.get_server(id="411833498207256576")
            room = ctx.message.channel
            MutedRole = discord.utils.get(ctx.message.server.roles, name="Muted")
            await bot.remove_roles(user, MutedRole)
            await bot.say(f"**{user.mention} got UnMuted (he he) by {ctx.message.author.mention} for __{Reason}__\nSee the logs in {LogRoom.mention}**")
            em = discord.Embed(title="UNMUTE", description=None, colour=0x1abc9c)
            em.add_field(name="User", value=f"{user.mention}")
            em.add_field(name="Moderator", value=f"{ctx.message.author}")
            em.add_field(name="Reason", value=f"{Reason}")
            em.set_author(name=user.name, icon_url=user.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(LogRoom, embed=em)
            Private = await bot.start_private_message(user)
            await bot.send_message(Private, f"**`Server: {botserver}`\nHey! You got unmuted, dont get too excited..**")
        
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number : int=None):
    if number is None:
        number = 1
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
        await bot.reply("**The usage is `-lock {duration (in sec)} {Reason}`**")
    elif duration is None:
        await bot.reply("**The usage is `-lock {duration (in sec)} {Reason}`**")
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
        await bot.reply("**The usage is `-unlock {Reason}`**")
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
async def dm(ctx, user : discord.User=None, *, text=None):
    if user is None:
        await bot.reply("**The usage is `-dm {user} {message}`**")
    elif text is None:
        await bot.reply("**The usage is `-dm {user} {message}`**")
    else:
        Private = await bot.start_private_message(user)
        await bot.send_message(Private, f"**`Server: {botserver}`\n{message}**")    

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
        await bot.reply("**The usage is `-roll {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `-roll {number} {number}`**")
    else:
        msg = random.randint(x, y)
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**My choose: {msg}**")

@bot.command(pass_context=True)
async def sub(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `-sub {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `-sub {number} {number}`**")
    else:
        msg = x - y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def mul(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `-mul {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `-mul {number} {number}`**")
    else:
        msg = x * y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def div(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `-div {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `-div {number} {number}`**")
    else:
        msg = x / y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def exp(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `-exp {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `-exp {number} {number}`**")
    else:
        msg = x ** y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command(pass_context=True)
async def add(ctx, x : int=None, y : int=None):
    if x is None:
        await bot.reply("**The usage is `-add {number} {number}`**")
    elif y is None:
        await bot.reply("**The usage is `-add {number} {number}`**")
    else:
        msg = x + y
        text = await bot.send_message(ctx.message.channel, "**Hmmm...**")
        await asyncio.sleep(3)
        await bot.edit_message(text, f"**The result: {msg}**")
    
@bot.command()
async def game(*, play=None):
    if play is None:
        await bot.reply("**The usage is `-game {Something to set as a game}`**")
    else:
        await bot.change_presence(game=discord.Game(name=play))
        em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
        await bot.say(embed=em)

@bot.command(pass_context=True)
async def nick(ctx, *, name=None):
    if name is None:
        await bot.reply("**The usage is `-name {Something to set as your name}`**")
    else:
        await bot.change_nickname(ctx.message.author, name)
        em = discord.Embed(title="Nickname", description=f"{ctx.message.author}'s nick set to __{name}__!", colour=0x3498db)
        await bot.say(embed=em)
    
@bot.command(pass_context=True)
async def suggest(ctx, pref=None, *, text=None):
    channel = bot.get_channel(id="426733808205692928")
    if pref is None:
        await bot.reply("**The usage is `-suggest {prefix (I, Q, S, C, B)} {text}`**")
    elif text is None:
        await bot.reply("**The usage is `-suggest {prefix (I, Q, S, C, B)} {text}`**")
    else:
        try:
            if pref is "I":
                msg = "IDEA"
                channel = bot.get_channel(id="547819227290271754")
            if pref is "S":
                msg = "SUGGESTION"
            if pref is "Q":
                msg = "QUESTION"
            if pref is "C":
                msg = "COMMAND SUGGESTION"
            if pref is "B":
                msg = "BUGS"
            else:
                bot.say("**Please use a valid prefix! The available prefixes: __I__dea, __Q__uestion, __S__uggestion, __C__ommand Suggestion, __B__ug report**")
        finally:
            colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
            col = random.choice(colours)
            em = discord.Embed(title=f"{msg}", description=f"**From {ctx.message.author.mention}**\n⋙ {text}", colour=col)
            em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
            em.set_footer(text=timer)
            await bot.send_message(ctx.message.channel, f"**:white_check_mark: Sent in {channel.mention}**")
            mesg = await bot.send_message(channel, embed=em)
            if pref is "S":
                await bot.add_reaction(mesg, "👍")
                await bot.add_reaction(mesg, "👎")
            if pref is "C":
                await bot.add_reaction(mesg, "👍")
                await bot.add_reaction(mesg, "👎")
            if pref is "I":
                await bot.add_reaction(mesg, "👍")
                await bot.add_reaction(mesg, "👎")

@bot.event
async def on_message(message):
    if message.content.startswith('-lenny'):
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        lenny = random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
        await bot.send_message(message.channel, "**A wild Lenny has appeard:**\n\n\t" + lenny)
    if message.content.startswith('-oof'):
        o = ['o00', 'oo', 'oO', 'o0', 'Oo', '0o', 'OOo', 'O0o', 'ooO', 'oo0', 'oo0oO', 'o0o', '0ooO', 'oo0oOO', 'ooo', '0oo', 'oooo', 'Ooo0', 'O0oo', 'ooo0', ]
        f = ['f', 'ff', 'fff']
        mark = ['!', '!!', '!!', '!1', '!!1', '!1!!', '1!!!', '!1!1!', '1!', '!!1!', '!!!1!', '!!!!', '!11!']
        msg1 = random.choice(o)
        msg2 = random.choice(f)
        msg3 = random.choice(mark)
        await bot.send_message(message.channel, msg1 + msg2 + msg3)
    if message.content.startswith('-8ball'):
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
    if message.content.startswith("-time"):
        timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        await bot.send_message(message.channel, f"**{message.author.mention}, the time is __{timer}__**")
    if message.content.startswith("-mod"):
        em = discord.Embed(title="MODERATION COMMANDS", description=None, colour=0x3498db)
        em.add_field(name="Admin commands", value=":notepad_spiral: -ban {member} {0 - 7 amount of days to delete his messages} \"{Reason}\"\n"
                     ":bulb: Kicks the user and removes his messages for the given days, the user can't rejoin, until he gots unbanned\n"
                     "\n"
                     ":notepad_spiral: The Unban command doesn't works, sorry about that. You need to unban the user from `Server Settings->Bans`\n"
                     ":bulb: UnBans the Banned user, the user now can rejoin by instant-invite links\n\n\n")
        em.add_field(name="Mod commands", value=":notepad_spiral: -kick {member} \"{Reason}\"\n"
                     ":bulb: Kicks the user from the server, the user can rejoin by instant-invite links\n"
                     "\n"
                     ":notepad_spiral: -mute {member} {duration(in sec)} \"{Reason}\"\n"
                     ":bulb: Mutes the user, this user can't send messages for the given duration, if the _time is up,_ he will auto get unmuted\n"
                     "\n"
                     ":notepad_spiral: -unmute {member} \"{Reason}\"\n"
                     ":bulb: UnMutes the Muted user, this user now allowed to send messages\n"
                     "\n"
                     ":notepad_spiral: -lock \"{Reason}\"\n"
                     ":bulb: Locks down the currently channel, only Admins can send messages until an unlock\n"
                     "\n"
                     ":notepad_spiral: -unlock \"{Reason}\"\n"
                     ":bulb: Unlocks the currently locked channel, now everyone can send messages there")
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith("-commands"):
        emb = discord.Embed(title="COMMANDS", description="Check my commands!", colour=0x95a5a6)
        emb.add_field(name='------------------------', value=":notepad_spiral:  -commands\n"
                      "Shows this message\n"
                      "\n"
                      ":notepad_spiral: -help\n"
                      "\n"
                      ":notepad_spiral: -tag\n"
                      "\n"
                      ":notepad_spiral: -nick {name}\n"
                      ":bulb: Set your nickname\n"
                      "\n"
                      ":notepad_spiral: -time\n"
                      ":bulb: Returns the real time in UTC+0!\n"
                      "\n"
                      ":notepad_spiral: -game {game}\n"
                      ":bulb: Set a game for the Bot\n"
                      "\n"
                      ":notepad_spiral: -mod\n"
                      ":bulb: The Moderation commands\n"
                      "\n"
                      ":notepad_spiral: -8ball\n"
                      ":bulb: Get answer (or not :>  ) to your question", inline=True)
        emb.set_thumbnail(url="https://cdn.discordapp.com/avatars/450246060456148993/b9fc7c3ec4dc905cc575ab313a7dba0c.webp?size=2048")
        emb.set_footer(text='------------------------')
        await bot.send_message(message.channel, embed=emb)
    await bot.process_commands(message) #IMPORTANT






token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
