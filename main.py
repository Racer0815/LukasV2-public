import discord
import json
import os
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    channel = client.get_channel(922861978484097056)
    await channel.send(f'Bot erfolgreich eingeloggt als {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Bann den Admin :)'))


@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name:
                    role = discord.utils.get(client.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(client.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

                await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


@client.command()
async def reactrole(ctx, emoji, role: discord.Role, *, message):
    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {
            'role_name': role.name,
            'role_id': role.id,
            'emoji': emoji,
            'message_id': msg.id
        }

        data.append(new_react_role)
    with open('reactrole.json', 'w') as j:
        json.dump(data, j, indent=4)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
