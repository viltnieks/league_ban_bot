import discord, time, asyncio

intents = discord.Intents.default()
intents.members = True
intents.presences = True

# server and channel id for logging if the trolling has been commited
LOG_SERVER = 
LOG_CHANNEL = 

# Makes a client
client = discord.Client(intents=intents)

start_time = time.time()

NoneType = type(None)
                    

# When the bot is ready

async def log_msg(msg):
    g = client.get_guild(LOG_SERVER)
    ch = g.get_channel(LOG_CHANNEL)
    await ch.send(msg)


async def wait_and_ban(m: discord.Member):
    print(f"{m.display_name} has been detected playing league of legends")
    await log_msg(f'{m.display_name} has been detected playing league')
    await asyncio.sleep(1800) # 30 (m) x 60 (s) = 1800 nu basic matene vispar lol
    g: discord.Guild = m.guild
    m: discord.Member = g.get_member(m.id)
    shall_ban = False
    for a in m.activities: # iteretes through his new activities and checks if hes still playing league 
        if a.name is not NoneType: # citadi vins dazriez prosta crasho nu gnjau custom activity kkas idfk ez fix
            if a.name.lower() == 'league of legends':
                shall_ban = True # designate the person for a ban

    if shall_ban:
        print(f"{m.display_name} has been banned from {g.name}")
        await m.send(f"You have been banned from {g.name} for playing too much League of Legends")
        await g.ban(m, reason="played league", delete_message_days=0)
        await log_msg(f'{m.display_name} has been banned from {g.name} for playing league')
    else:
        print(f"{m.display_name} has closed the game timely")


@client.event
async def on_ready():
    print(f'{client.user} - online')
    await log_msg(f'{client.user} is now online')


@client.event
async def on_member_update(before, after):
    for a in after.activities:
        if a.name.lower() == 'league of legends':
            await wait_and_ban(after)

# When someone msges smth
@client.event
async def on_message(message):
    # Checks if we sent the msg
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

    if message.content.startswith('$uptime'):
            time_elapsed = int(time.time() - start_time)
            m, s = divmod(time_elapsed, 60)
            h, m = divmod(m, 60)
            await message.channel.send('{:d}:{:02d}:{:02d}'.format(h, m, s))



from important import TOKEN # token stored on an local file :)
client.run(TOKEN)
