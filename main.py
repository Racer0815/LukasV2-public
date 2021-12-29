import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is logged in.")
    channel = client.get_channel(922861978484097056)
    await channel.send('Bot erfolgreich eingeloggt')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='diesem Server'))
    await channel.send("hier reagieren")



async def on_reaction_add(self, reaction, user):
    test = discord.utils.get(user.guild.roles, name="1")
    if str(reaction.emoji) == ":✅":
        await user.add_roles(test)
    else:
        print("error")

client.run("token")