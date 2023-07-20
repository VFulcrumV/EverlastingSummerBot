import disnake
from disnake.ext import commands

from db_data import checking, db_session
from cogs_data import buttons, modals, variables_images, variables

from __functions import functions


class CMDModerators(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = db_session.create_session()

    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def edit_greeting(self, inter: disnake.AppCmdInter):
        greeting = self.session.query(checking.Greeting).filter(checking.Greeting.id == 2).first()

        embed = functions.get_greeting_embed(greeting, inter, False)

        functions.set_footer(embed, inter.guild, greeting)

        view = buttons.GreetingButtons(inter.author)
        message = await inter.response.send_message(embed=embed, view=view)
        view.message = message


    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    async def send_agreement(self, inter: disnake.AppCmdInter):



def setup(bot):
    bot.add_cog(CMDModerators(bot))