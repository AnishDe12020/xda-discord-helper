import discord, os
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv import load_dotenv

load_dotenv()

activity = discord.Streaming(name="xda/help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ/")
client = commands.Bot(command_prefix = "axda/", activity = activity, intents=discord.Intents.all())
client.remove_command("help")
slash = SlashCommand(client, sync_commands=True)

guild_ids = os.environ["SLASH_GUILD_IDS"]
guild_ids = guild_ids.split(" ")
guild_ids = [int(guild_id) for guild_id in guild_ids]

# def main():



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
        
        
for file in os.listdir('./cogs'):
    if file.endswith(".py"):
        client.load_extension(f"cogs.{file[:-3]}")
    
    
client.run(os.environ["BOT_TOKEN"])
