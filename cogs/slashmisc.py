import discord, os, googlesearch, asyncio
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="xda/", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

guild_ids = os.environ["SLASH_GUILD_IDS"]
guild_ids = guild_ids.split(" ")
guild_ids = [int(guild_id) for guild_id in guild_ids]

class SlashMisc(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    @cog_ext.cog_slash(name="magisk", 
             description="Sends everything Magisk related",
             guild_ids=guild_ids)
    async def _magisk(self, ctx):
        whatismagisk = discord.Embed(title = "__Magisk: The magic mask of Android__", color = 0x301c24, url = "https://github.com/topjohnwu/Magisk")
        whatismagisk.add_field(name = "What is Magisk?", value = "In simple terms, Magisk is a way to root your phone systemlessly and install *modules* on it. It also allows you to bypass Safetynet checks while you're rooted.", inline = False)
        whatismagisk.add_field(name = "Should I use it compared to SuperSU and others?", value = "YES! SuperSU is quite outdated nowadays and others range from not-well-reputable to downright spyware.", inline = False)
        whatismagisk.add_field(name = "How do I install it on my phone?", value = "Make sure you have bootloader unlocked, then check out the installation guide for more info\n", inline = False)
        whatismagisk.set_thumbnail(url = "https://cdn.discordapp.com/attachments/867824004072210452/868167290628210739/download.jpg")
        await ctx.send(embed = whatismagisk)

        embed = discord.Embed(title = "__Magisk related links:__", color = 0x301c24)
        embed.add_field(name = "Download Link", value = "https://github.com/topjohnwu/Magisk/releases", inline = False)
        embed.add_field(name = "Official Installation Guide", value = "https://topjohnwu.github.io/Magisk/install.html", inline = False)
        embed.add_field(name = "Magisk Documentation (Users and Devs)", value = "https://topjohnwu.github.io/Magisk/", inline = False)
        await ctx.send(embed = embed)
        
    @cog_ext.cog_slash(name="remind", 
             description="Experimental: Reminds you of <insert thing> after n seconds",
             guild_ids=guild_ids)
    async def remind(self, ctx, time, msg):
        """Reminds you of something after a certain amount of time"""
        await ctx.defer()
        uid = ctx.author.id
        await ctx.send("Reminding you in {} seconds".format(time))
        await asyncio.sleep(int(time))
        await ctx.send(f'<@{uid}> Reminder: {msg}')

    @cog_ext.cog_slash(name="ping", description="Just a test command",
            guild_ids=guild_ids)
    async def _ping(self, ctx): 
        await ctx.send(f"Pong! {round(self.client.latency*1000)}ms")
        
def setup(client):
    client.add_cog(SlashMisc(client))