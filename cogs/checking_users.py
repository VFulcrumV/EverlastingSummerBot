import disnake
from disnake.ext import commands

from db_data import db_session
from db_data import checking

from __functions import functions

from cogs_data import variables


class Checking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = db_session.create_session()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        greeting = self.session.query(checking.Greeting).first()

        embed = functions.get_greeting_embed(greeting, member, True)

        if greeting.role:
            role = disnake.utils.get(member.guild.roles, id=greeting.role)
            await member.add_roles(role)

        if greeting.send_channel:
            channel = disnake.utils.get(member.guild.channels, id=greeting.send_channel)
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Checking(bot))