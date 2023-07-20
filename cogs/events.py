from disnake.ext import commands


from cogs_data import buttons

from db_data import checking, db_session


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            self.bot.add_view(buttons.GreetingButtons())
            self.persistent_views_added = True

        cur = db_session.create_session()

        greeting = cur.query(checking.Greeting).first()
        agreement = cur.query(checking.Agreement).first()

        if greeting is None:
            greeting = checking.Greeting()
            cur.add(greeting)
            greeting = checking.Greeting()
            cur.add(greeting)

        if agreement is None:
            agreement = checking.Agreement()
            cur.add(agreement)
            agreement = checking.Agreement()
            cur.add(agreement)
            
        cur.commit()

        print(f'Bot {self.bot.user} is ready to work!')

    # @commands.Cog.listener()
    # async def on_slash_command_error(self, ctx, error):
    #     if isinstance(error, commands.errors.MissingPermissions):
    #         await ctx.response.send_message('Команда для администраторов', ephemeral=True)


def setup(bot):
    bot.add_cog(Events(bot))