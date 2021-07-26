import discord, asyncio
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def magisk(self, ctx, links="asdf"):
        if links == "asdf":
            whatismagisk = discord.Embed(title = "__Magisk: The magic mask of Android__", color = 0x301c24, url = "https://github.com/topjohnwu/Magisk")
   
            whatismagisk.add_field(name = "What is Magisk?", value = "In simple terms, Magisk is a way to root your phone systemlessly and install *modules* on it. It also allows you to bypass Safetynet checks while you're rooted.", inline = False)
            whatismagisk.add_field(name = "Should I use it compared to SuperSU and others?", value = "YES! SuperSU is quite outdated nowadays and others range from not-well-reputable to downright spyware.", inline = False)
            whatismagisk.add_field(name = "How do I install it on my phone?", value = "Make sure you have bootloader unlocked, then check out the installation guide for more info\n", inline = False)
            whatismagisk.set_thumbnail(url = "https://cdn.discordapp.com/attachments/867824004072210452/868167290628210739/download.jpg")
            await ctx.send(embed = whatismagisk)
        else:
            embed = discord.Embed(title = "__Magisk related links:__", color = 0x301c24)

            embed.add_field(name = "Download Link", value = "https://github.com/topjohnwu/Magisk/releases", inline = False)
            embed.add_field(name = "Official Installation Guide", value = "https://topjohnwu.github.io/Magisk/install.html", inline = False)
            embed.add_field(name = "Magisk Documentation (Users and Devs)", value = "https://topjohnwu.github.io/Magisk/", inline = False)
            await ctx.send(embed = embed)
    
    @commands.command()
    async def remind(self, ctx, time, *msg):
        """Reminds you of something after a certain amount of time"""
        uid = ctx.author.id
        await ctx.send("Reminding you in {} seconds".format(time))
        await asyncio.sleep(int(time))
        await ctx.send(f'<@{uid}> Reminder: {" ".join(msg)}')
        
        
def setup(client):
    client.add_cog(Misc(client))