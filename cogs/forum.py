import discord
import googlesearch
from discord.ext import commands

num = [1, 2, 3, 4, 5]

class Forum(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["forums", "search"])
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def forum(self, ctx, *srch):  

        embed = self.search(srch, xda=True)
        await ctx.send(embed = embed)
        
    @commands.command()
    @commands.cooldown(1, 45, commands.BucketType.user)
    async def google(self, ctx, *srch):  

        embed = self.search(srch)

        await ctx.send(embed = embed)

    def search(self, srch=[], xda=False):
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
    client.add_cog(Forum(client))