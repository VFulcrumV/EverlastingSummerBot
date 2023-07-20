import disnake

from cogs_data import variables, variables_images



def get_hex(color):
    return eval(f'0x{color[1:]}')


async def check_available(self, inter):
    if self.author is not None:
        await inter.response.send_message(
            'Вы не можете взаимодействовать с командой другого пользователя', ephemeral=True)
    else:
        await inter.response.edit_message(
            'Бот был перезапущен, команда недействительна', embed=None, view=None)
        await inter.delete_original_message(delay=3)


def get_greeting_embed(greeting, member, flag):
    embed = disnake.Embed(title='', description='')
    if greeting.title:
        if flag and '@User' in greeting.title:
            edited_text = edit_user_mention_text(greeting.title)
            embed.title = eval(edited_text)
        else:
            embed.title = greeting.title
    if greeting.description:
        if flag and '@User' in greeting.description:
            edited_text = edit_user_mention_text(greeting.description)
            embed.description = eval(edited_text)
        else:
            embed.description = greeting.description
    if greeting.color_embed:
        embed.colour = get_hex(greeting.color_embed)
    if greeting.thumbnail:
        embed.set_thumbnail(url=greeting.thumbnail)
    if greeting.image:
        embed.set_image(url=greeting.image)
    if greeting.info_channel:
        greeting_chanel = disnake.utils.get(member.guild.channels, id=int(greeting.info_channel))
        embed.add_field(name="Не забудь заглянуть сюда:", value=greeting_chanel.mention, inline=True)

    return embed


def copy_greeting_params(first, second):
    print(first.title, second.title)
    first.title = second.title
    print(first.title, second.title)
    first.description = second.description
    first.thumbnail = second.thumbnail
    first.image = second.image
    first.info_channel = second.info_channel
    first.send_channel = second.send_channel
    first.role = second.role
    first.color_embed = second.color_embed


def set_footer(embed, guild, greeting):
    send_channel = disnake.utils.get(guild.channels, id=greeting.send_channel)
    role = disnake.utils.get(guild.roles, id=greeting.role)

    info_list = []
    if send_channel is None:
        send_channel_mention = None
    else:
        send_channel_mention = send_channel.name
        info_list.append(send_channel_mention)
    if role is None:
        role_mention = None
    else:
        role_mention = role.name
        info_list.append(role_mention)

    if info_list:
        info = '[' + ', '.join(info_list) + ']'
    else:
        info = ''

    embed.set_footer(
        text=f'Пример поста {info}',
        icon_url=variables_images.post_example_icon
    )


def edit_user_mention_text(text):
    if '@User' in text:
        new_text = text.split('@User')
        return "f'" + "{member.mention}".join(new_text) + "'"
