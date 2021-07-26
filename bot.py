import discord, os
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv

load_dotenv()

activity = discord.Streaming(name="xda/help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ/")
client = commands.Bot(command_prefix = "xda/", activity = activity, intents=discord.Intents.all())
client.remove_command("help"); slash = SlashCommand(client, sync_commands=True); num = [1, 2, 3, 4, 5]

guild_ids = os.environ["SLASH_GUILD_IDS"]
guild_ids = guild_ids.split(" ")
guild_ids = [int(guild_id) for guild_id in guild_ids]


###########################################################
"""Ping commands"""
@slash.slash(name="ping", description="Just a test command",
         guild_ids=guild_ids)
async def _ping(ctx): 
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")
        
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")
###########################################################


@client.command()
@commands.has_role("Helper")
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
@commands.has_role("Helper")
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    
    
@client.command()
@commands.has_role("Helper")
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    
    
##########################################################################################
"""Error Handling"""
@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(embed = discord.Embed(title = "You do not have the __Helper__ role", color = 0x000000))
    else:
        raise error
        
@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(embed = discord.Embed(title = "You do not have the __Helper__ role", color = 0x000000))
    else:
        raise error
        
        
@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(embed = discord.Embed(title = "You do not have the __Helper__ role", color = 0x000000))
    else:
        raise error
##########################################################################################       
        
        
for file in os.listdir('./cogs'):
    if file.endswith(".py"):
        client.load_extension(f"cogs.{file[:-3]}")
    
    
client.run(os.environ['BOT_TOKEN'])
