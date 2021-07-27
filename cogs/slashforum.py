import discord, os, googlesearch
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from dotenv import load_dotenv

load_dotenv()

num = [1, 2, 3, 4, 5]
bot = commands.Bot(command_prefix="xda/", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

guild_ids = os.environ["SLASH_GUILD_IDS"]
guild_ids = guild_ids.split(" ")
guild_ids = [int(guild_id) for guild_id in guild_ids]

class SlashForum(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    @cog_ext.cog_slash(name="google", 
             description="Searches Google for you",
             guild_ids=guild_ids)
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def _google(self, ctx: SlashContext, search_string):
        await ctx.defer()

        search_string = search_string.split(" ")

        embed = self.search(search_string)
        await ctx.send(embed = embed)

    @cog_ext.cog_slash(name="forum", 
             description="Searches XDA Forums for you",
             guild_ids=guild_ids)
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def _forum(self, ctx: SlashContext, search_string):
        await ctx.defer()

        search_string = search_string.split(" ")

        embed = self.search(search_string, xda=True)

        await ctx.send(embed = embed)

    def search(self, srch, xda=False):
        param = " ".join(srch)
        if xda:
            param += " site:forum.xda-developers.com"

        embed = discord.Embed(title = "__Here are the results for your search:__", color = 0x301c24)
        search_url = list(googlesearch.search(param, num_results=5))

        for links, n in zip(search_url, num):
            embed.add_field(name = f"Link #{n}:", value = links, inline=False)
        embed.set_footer(text = "Hope you found what you're looking for")

        return embed
     
def setup(client):
    client.add_cog(SlashForum(client))