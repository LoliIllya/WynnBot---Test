from discord.ext import commands
import discord

class Events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # ----- Handling errors -----
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all requirements :rolling_eyes:.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have all the requirements :angry:")
        else:
             print(error)

    # ----- Making commands case insensitive -----
    @commands.Cog.listener()
    async def on_message(self, message):
        temp = message.content.split(" ")
        message.content = str(temp[0].lower())
        for x in temp[1:]:
            message.content += " " + str(x)

    # ----- Giving out Guest role when user joins -----
    @commands.Cog.listener()
    async def on_member_join(self,member):
        try:
            await member.add_roles(discord.utils.get(member.guild.roles, name='guest')) 
        except Exception as e:
            await print('Cannot assign role. Error: ' + e)
        await bot.process_commands(message)


def setup(bot):
    bot.add_cog(Events(bot))
