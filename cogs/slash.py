import discord 
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash import cog_ext
from time import time

bot = commands.Bot(command_prefix="xda/", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True); startTime = time()

class Slashmain(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @cog_ext.cog_slash(name="about", 
             description="Some statistics about the bot",
             guild_ids=[868353576160854116, 422814981520621569])
    async def _about(self, ctx: SlashContext): 
        uptime_s = int(round(time() - startTime))
        if uptime_s > 86400:
            uptime = str(uptime_s // 86400)
            if uptime == "1": uptime += " day"
            else: uptime += " days"
        elif uptime_s > 3600:
            uptime = str(uptime_s // 3600)
            if uptime == "1": uptime += " hour"
            else: uptime += " hours"
        elif uptime_s > 60:
            uptime = str(uptime_s // 60)
            if uptime == "1": uptime += " minute"
            else: uptime += " minutes"
        else:
            uptime = str(uptime_s)
            uptime += " seconds"

        embed = discord.Embed(title = "XDA Helper statistics", color = 0x301c24)
        embed.add_field(name = "Revision", value = "v1.0-stable")
        embed.add_field(name = "Uptime", value = uptime)
        await ctx.send(embed = embed)
     
def setup(client):
    client.add_cog(Slashmain(client))