import logging
import disnake
from disnake.ext import commands

from typing import Optional

bot = commands.Bot(
    command_prefix='ff-',
    help_command=None,
    intents=disnake.Intents.all(),
    test_guilds=[1004582832687034418]
)

#Drops
class DropDown(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Burger', description='b', emoji='🍔'),
            disnake.SelectOption(label='Turger', description='d', emoji='🍕'),
            disnake.SelectOption(label='Murger', description='v', emoji='🥓')
        ]
        super().__init__(
            placeholder='Menu',
            min_values=1,
            max_values=2,
            options=options
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.send_message(f'order: {self.values[0]}')


class DropDownView(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropDown())


#Buttons
class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = Optional[bool]

    @disnake.ui.button(
        label='Confirm',
        style=disnake.ButtonStyle.green,
        emoji='🍦')
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = True
        self.stop()

    @disnake.ui.button(
        label='Cancel',
        style=disnake.ButtonStyle.red,
        emoji='🍦')
    async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = False
        self.stop()

    @disnake.ui.button(
        label='just button',
        style=disnake.ButtonStyle.red,
        emoji='🍦',
        row=1)
    async def butt(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        self.value = 4
        self.stop()


#Link
class Link(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(disnake.ui.Button(
            label='link',
            url='https://cdn.discordapp.com/attachments/1048240211320123402/1088859213989691534/-Sg9t_dv-L4.jpg'))


#Events
@bot.event
async def on_ready():
    print(f'Bot {bot.user} is ready to work.')


@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1092065599540187209)
    channel = member.guild.system_channel
    embed = disnake.Embed(
        title='New member',
        description=f'{member.name}#{member.discriminator}',
        color=0x00ffff
    )
    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author != bot.user:
        if f'{message.content}' == '':
            await message.delete()
        else:
            await message.guild.system_channel.send(f'{message.author.mention} send: "{message.content}"')


@bot.event
async def on_command_error(ctx, error):
    print(error, type(error))
    if isinstance(error, commands.CommandInvokeError):
        await ctx.channel.send(f'{ctx.author.mention}, you have not freedom')
    elif isinstance(error, commands.UserInputError):
        await ctx.send(
            embed=disnake.Embed(
                description=f'Правильное использование команды: '
                            f'{ctx.prefix}{ctx.command.name} ({ctx.command.brief})'
                            f'\nПример: {ctx.prefix}{ctx.command.usage}'
            )
        )


#Commands
@bot.command(name='кик', aliases=['лох', 'банан', 'kick'], brief='aboba', usage='kick <@user> <reason>')
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason='лох'):
    await ctx.send(
        f'{ctx.author.mention} выгнал {member.mention}', delete_after=2
    )
    await ctx.message.delete(delay=2)
    await member.kick(reason=reason)


#Slash Commands
@bot.slash_command()
async def calc(inter, expression: str):
    await inter.send(str(eval(expression)))
    buttons = Confirm()
    embed = disnake.Embed(
        title='New member',
        description=f'Yes?',
        color=0x00ffff
    )
    await inter.send(embed=embed, view=buttons)
    await buttons.wait()

    if buttons.value is None:
        await inter.send('pppppppp')
    elif buttons.value is True:
        await inter.send('get link', view=Link())
    elif buttons.value == 4:
        await inter.send('fourrrrrrr')
    else:
        await inter.send('loh')


@bot.slash_command()
async def delivery(inter):
    await inter.send('Yours order:', view=DropDownView())


if __name__ == '__main__':
    bot.run('token')