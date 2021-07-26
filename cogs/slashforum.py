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
    async def _google(self, ctx: SlashContext, search_string):
        await ctx.defer()

        embed = discord.Embed(title = "__Here are the results for your search:__", color = 0x301c24)
        search_url = list(googlesearch.search(search_string, num_results=10)); del search_url[5:]
    
        for links, n in zip(search_url, num):
            embed.add_field(name = f"Link #{n}:", value = links, inline=False)
        embed.set_footer(text = "Hope you found what you're looking for")
        await ctx.send(embed = embed)

    @cog_ext.cog_slash(name="forum", 
             description="Searches XDA Forums for you",
             guild_ids=guild_ids)
    async def _forum(self, ctx, search_string):
        serch_a = search_string; await ctx.defer()
        serch_a += " site:forum.xda-developers.com"
    
        embed = discord.Embed(title = "__Here are the results for your search:__", color = 0x301c24)
        search_url = list(googlesearch.search(serch_a, num_results=10)); del search_url[5:]
    
        for links, n in zip(search_url, num):
            embed.add_field(name = f"Link #{n}:", value = links, inline=False)
        embed.set_footer(text = "Happy modding :)")
        await ctx.send(embed = embed)
     
def setup(client):
    client.add_cog(SlashForum(client))