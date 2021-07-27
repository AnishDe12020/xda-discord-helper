import discord
from discord.ext import commands

class CogsLoader(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("Helper")
    async def load(self, ctx, extension):
        self.client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}")

    @commands.command()
    @commands.has_role("Helper")
    async def unload(self, ctx, extension):
        self.client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}")

    @commands.command()
    @commands.has_role("Helper")
    async def reload(self, ctx, extension):
        self.client.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}")

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

def setup(client):
    client.add_cog(CogsLoader(client))