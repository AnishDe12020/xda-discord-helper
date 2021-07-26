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
        print(f"\nStarted at {datetime.now().strftime('%I:%m %p')}\nBot Creator(s): NullCode#1337; Nabsi#4017; justAHuman#1202\n\n")
    
        guild_ids_of_guilds_bot_is_in = []

        for guild in self.client.guilds:
            guild_ids_of_guilds_bot_is_in.append(guild.id)

        print("IDs of servers the bot is in:\n", guild_ids_of_guilds_bot_is_in)
        print("Errors:")


    @commands.command(aliases=['help', 'helpmenu'])
    async def menu(self, ctx):
        embed = discord.Embed(title = "__Commands List:__", color = 0x301c24)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/868353576160854120/869269123861999707/XDA.png")
        embed.add_field(name = "xda/google {question}", value = "Searches Google for you", inline = False)
        embed.add_field(name = "xda/forum {question}", value = "Searches XDA Forums for your string", inline = False)
        embed.add_field(name = "xda/magisk {links} [Optional]", value = "Sends everything [and links] Magisk related", inline = False)
        embed.add_field(name = "xda/remind {seconds} {msg}", value = "Reminds you after x seconds with a message", inline = False)
        embed.add_field(name = "xda/about {no arguments}", value = "About the bot and it's creator :D", inline = False)
        embed.add_field(name = "xda/ping {no arguments}", value = "Sends client latency", inline = False)
        embed.add_field(name = "xda/help {no arguments}", value = "Shows this message", inline = False)
        await ctx.send(embed = embed)
    
    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
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
        embed.add_field(name = "Revision", value = "v1.0-stable", inline = False)
        embed.add_field(name = "Uptime", value = uptime, inline = False)
        embed.add_field(name = "Source Code", value = "[On Github](https://github.com/NullCode13/xda-discord-helper/)", inline = False)
        embed.add_field(name = "Heroku Build Status", value = "Passing", inline = False)
        await ctx.send(embed = embed)
        
        e2 = discord.Embed(title = "About the bot's creators")
        e2.add_field(name = "Who are they?", value = "NullCode, justAhuman, Nabsi and Otus9051")
        e2.add_field(name = "What do they do?", value = "As of now, we are students who are extremely bored")
        e2.set_footer(text = "If you want to contribute, feel free to PR in the git repo")
        embed.set_image(url="https://cdn.discordapp.com/attachments/868353576160854120/869268253745250324/unknown.png")
        await ctx.send(embed = e2)
        
def setup(client):
    client.add_cog(Main(client))
