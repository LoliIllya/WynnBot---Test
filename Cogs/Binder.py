from discord.ext import commands

from Wrappers.player import player
import bot_data as bd


# TODO: Check how well it works
class Binder(commands.Cog):  # TODO: Documentation
    player_list = {}

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Waiting for 1.20 API update
    # @commands.command(description="????", usage="!bind <username> <guild> <highest_level>")
    async def bind(self, ctx: commands.Context, username: str, guild_name: str, highest_lvl: int):

        Binder.player_list = Binder.get_binds()  # Update the list; No, I don't have a better alternative

        if ctx.author.id in Binder.player_list:
            await ctx.channel.send(
                embed=bd.error_embed('user error', f'Member \"{ctx.author.mention}\" is already bound'))
            return

        player_data = player(username)  # get the data from wynncraft API
        if player is None:  # if the player doesn't exist -> error
            await ctx.channel.send(
                embed=bd.error_embed('User error', f'Player name \"{username}\" does not exist'))
            return

        if player_data['guild name'] != guild_name:  # if incorrect guild -> error
            await ctx.channel.send(
                embed=bd.error_embed('User error', f'Player \"{username}\" is not in guild \"{guild_name}\"'))
            return

        if player_data['highest level combat'] != highest_lvl:  # if incorrect highest level -> error
            await ctx.channel.send(
                embed=bd.error_embed('User error', f'Highest level of {username} is not \"{highest_lvl}\"'))
            return

        Binder.player_list[ctx.author.id] = username  # add player to the list
        Binder.set_binds()  # save the new bind

        await ctx.channel.send(f'Member {ctx.author.mention} was bound to name {username}')
        await ctx.channel.send(str(Binder.player_list))

    @staticmethod
    def get_binds() -> dict:
        """
        Gets the list of bound members and returns it
        """
        with open('player_bind.txt', 'r') as f:
            return eval(f.read())

    @staticmethod
    def set_binds():
        """
        Updates the file with the list of bound members
        """
        with open('player_bind.txt', 'w') as f:  # write it into a file
            f.write(str(Binder.player_list).replace('\'', '\"'))


def setup(bot: commands.Bot):
    """
    Add the "Events" class to the bot
    """
    bot.add_cog(Binder(bot))
