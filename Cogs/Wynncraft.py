from discord.ext import commands
import discord
import requests as req

class Wynncraft(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    # ----- player stats -----
    @commands.command(help="Let's you view a player's profile.") # Need to make it look better
    async def profile(self, ctx, PlayerName):

        resp = req.get(f'https://api.wynncraft.com/v2/player/{PlayerName}/stats')
        # get the data
        data = resp.json()['data'][0]
        # print the data
        if resp['code'] == 400:
            return await ctx.channel.send('Cannot find user.') 
        highestlvl = 0
        for x in data['classes']:
            if x['professions']['combat']['level'] > highestlvl:
                highestlvl = x['professions']['combat']['level']
        embedVar = discord.Embed(title=f"{PlayerName}'s profile", color=0x00ff00)
        embedVar.add_field(name="UserName: ", value=f"{data['username']}", inline=True)
        embedVar.add_field(name="Rank: ", value=f"{data['meta']['tag']['value']}", inline=False)
        embedVar.add_field(name="Online: ", value=f"{data['meta']['location']['online']}", inline=True)
        embedVar.add_field(name="Server: ", value=f"{data['meta']['location']['server']}", inline=True)
        embedVar.add_field(name = chr(173), value = chr(173))
        embedVar.add_field(name="Guild's name: ", value=f"{data['guild']['name']}", inline=True)
        embedVar.add_field(name="Rank in guild: ", value=f"{data['guild']['rank']}", inline=True)
        embedVar.add_field(name="Playtime: ", value=f"{int((data[0]['meta']['playtime'] *4.7)/60)} hours.", inline=False)
        embedVar.add_field(name="Highest Level: ", value=f"{highestlvl}", inline=False)
        embedVar.add_field(name="Joined: ", value=f"{data['meta']['firstJoin'][:10]}", inline=True)
        await ctx.channel.send(embed=embedVar)
    
     # ----- guild stats -----
    @commands.command() #? Need to make it look better
    async def guild(self, ctx, GuildName):
        resp = req.get(f'https://api.wynncraft.com/public_api.php?action=guildStats&command={GuildName}')

        data = resp.json()

        if "error" in data:
            return await ctx.channel.send('Cannot find guild.') 

        embedVar = discord.Embed(title=f"{GuildName}", color=0xFF0000)
        embedVar.add_field(name="Name: ", value=f"{data['name']}", inline=False)
        embedVar.add_field(name="Prefix: ", value=f"{data['prefix']}", inline=False)
        embedVar.add_field(name="Level: ", value=f"{data['level']}", inline=False)
        embedVar.add_field(name="Members: ", value=f"{len(data['members'])}", inline=False)
        embedVar.add_field(name="Territories: ", value=f"{data['territories']}", inline=False)
        # embedVar.add_field(name="Playtime: ", value=f"{json['data'][0]['meta']['playtime'] /60} hours.", inline=False)
        embedVar.add_field(name="Created at: ", value=f"{data['createdFriendly']}", inline=False)
        await ctx.channel.send(embed=embedVar)

    # ----- item stats -----
    @commands.command(help="Shows you the stats of an item.") #! Need to finish this
    async def item(self, ctx, ItemName):
        resp = req.get(f'https://api.wynncraft.com/public_api.php?action=itemDB&search={ItemName}')
        data = resp.json()

def setup(bot):
    bot.add_cog(Wynncraft(bot))