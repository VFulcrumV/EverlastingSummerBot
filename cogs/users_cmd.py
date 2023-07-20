from typing import Optional

import disnake
from disnake.ext import commands


class CMDUsers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(CMDUsers(bot))
