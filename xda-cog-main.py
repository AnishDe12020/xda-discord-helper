import discord, os
from discord.ext import commands
from discord_slash import SlashCommand
from googlesearch import search as sr


activity = discord.Streaming(name="xda/help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ/")
client = commands.Bot(command_prefix = "xda/", activity = activity, intents=discord.Intents.all())
client.remove_command("help"); slash = SlashCommand(client, sync_commands=True); num = [1, 2, 3, 4, 5]
    
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    
    
@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    
    
for file in os.listdir('./cogs'):
    if file.endswith(".py"):
        client.load_extension(f"cogs.{file[:-3]}")
    
    
client.run("ODQ3MTAxMjI0NjU0MDc3OTky.YK5Kfg.Se8FELBKKcsFnYdUnrXGJ_Yos14")