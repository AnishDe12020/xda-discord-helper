import discord 
from discord.ext import commands
from datetime import datetime
from time import time

startTime = time()

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("""   _  _____  ___     ___  _                     __  __ __    __            
  | |/_/ _ \/ _ |   / _ \(_)__ _______  _______/ / / // /__ / /__  ___ ____
 _>  </ // / __ |  / // / (_-</ __/ _ \/ __/ _  / / _  / -_) / _ \/ -_) __/
/_/|_/____/_/ |_| /____/_/___/\__/\___/_/  \_,_/ /_//_/\__/_/ .__/\__/_/   
                                                           /_/            """)
        print(f"\nStarted at {datetime.now().strftime('%I:%m %p')}\nBot Creator(s): NullCode#1337; Nabsi#4017; justAHuman#1202\n\nErrors:")
    
    @commands.command(aliases=['help', 'helpmenu'])
    async def menu(self, ctx):
        embed = discord.Embed(title = "__Commands List:__", color = 0x301c24)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/422822063049539584/868149682088603678/XDA.png")
        embed.add_field(name = "xda/google {question}", value = "Searches Google for you", inline = False)
        embed.add_field(name = "xda/forum {question}", value = "Searches XDA Forums for your string", inline = False)
        embed.add_field(name = "xda/magisk", value = "Sends everything Magisk related", inline = False)
        embed.add_field(name = "xda/about", value = "About the bot and it's creator :D", inline = False)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def about(self, ctx):
        # Finding out bot uptime
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
    client.add_cog(Main(client))
