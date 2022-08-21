import asyncio

import discord
from datetime import datetime

# Change the token to your bot token
TOKEN = "Your Bot token here"
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    print("Current guilds / servers: \n")

    print("----------")

    for guild in client.guilds:
        print("ID: " + str(guild.id) + " | Name: " + guild.name)

        print("----------")
        print("All members: ")
        for m in guild.members:
            print(str(m) + " ID: " + str(m.id) + " [" + str(m.status) + "]")

    print("----------")

    # Uncomment these 2 lines if you don't want the server to be hardcoded
    # y = input("Input the id of the server you want to track: \n")
    # g = client.get_guild(int(y))

    i = input("Input the id of the user you want to track: \n")

    # Comment this line out if you don't want the server to be hardcoded
    # Also change the id if you want it hardcoded
    g = client.get_guild(123456789)

    m = g.get_member(int(i))

    print("----------")
    print("Logging started")
    print("----------")

    # Create the log file
    f = open("log.txt", "w")
    f.write("[Log for user: " + m.name + "]\n")
    f.write("----------\n\n")
    now = datetime.now()
    f.write("[" + str(now) + "]" + " Current status [" + str(m.status) + "]\n")

    # Check if the user changes his status
    while 1:
        stat_one = m.status
        await wait()
        stat_two = m.status

        if stat_one != stat_two:
            now = datetime.now()
            f.write("[" + str(now) + "] " + "Status changed from [" + str(stat_one) + "] to [" + str(stat_two) + "]\n")
            print("[" + str(now) + "] " + "Status changed from [" + str(stat_one) + "] to [" + str(stat_two) + "]")
        else:
            now = datetime.now()
            print("[" + str(now) + "] " + "Status did not change")


async def wait():
    # Change the time between status checks
    await asyncio.sleep(5)


client.run(TOKEN)
