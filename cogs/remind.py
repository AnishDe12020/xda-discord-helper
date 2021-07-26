import discord
from discord.ext import commands
import asyncio

class Remind(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remind(self, ctx, time, *msg):
        """Reminds you of something after a certain amount of time"""
        await ctx.send("I'll remind you of that in {} seconds".format(time))
        await asyncio.sleep(int(time))
        await ctx.send(" ".join(msg))

def setup(client):
    client.add_cog(Remind(client))