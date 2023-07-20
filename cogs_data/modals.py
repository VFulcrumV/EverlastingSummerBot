import disnake
from disnake import TextInputStyle


from db_data import db_session, checking

from cogs_data import variables_images, variables

from __functions import functions


class ModalGreetingInformation(disnake.ui.Modal):
    def __init__(self, inter):
        components = [
            disnake.ui.TextInput(
                label='title',
                placeholder='Длина заголовка не больше 200 символов',
                custom_id='title',
                style=TextInputStyle.paragraph,
                max_length=200,
            ),
            disnake.ui.TextInput(
                label='description',
                placeholder='Длина описания не больше 3500 символов',
                custom_id='description',
                style=TextInputStyle.paragraph,
                max_length=3500
            ),
            disnake.ui.TextInput(
                label='info channel',
                placeholder='ID канала',
                custom_id='info channel',
                style=TextInputStyle.paragraph,
                max_length=500
            ),
            disnake.ui.TextInput(
                label='send channel',
                placeholder='ID канала',
                custom_id='send channel',
                style=TextInputStyle.paragraph,
                max_length=500
            ),
            disnake.ui.TextInput(
                label='role',
                placeholder='ID роли',
                custom_id='role',
                style=TextInputStyle.paragraph,
                max_length=500
            )
        ]
        super().__init__(title='Set greeting information', components=components)

        self.session = db_session.create_session()
        self.inter = inter

    async def callback(self, inter: disnake.ModalInteraction):
        greeting = self.session.query(checking.Greeting).filter(checking.Greeting.id == 2).first()

        for key, value in inter.text_values.items():
            true_key = '_'.join(key.split())
            print(key, value)
            if value.lower() == '-':
                exec(f'greeting.{true_key} = None')
            elif value.lower() == 'same':
                pass
            else:
                exec(f'greeting.{true_key} = "{value}"')
        self.session.commit()

        embed = functions.get_greeting_embed(greeting, self.inter, False)

        functions.set_footer(embed, self.inter.guild, greeting)

        await self.inter.edit_original_message(embed=embed)
        await inter.send('Информация внесена', delete_after=2)


class ModalGreetingDecoration(disnake.ui.Modal):
    def __init__(self, inter):
        components = [
            disnake.ui.TextInput(
                label='thumbnail',
                placeholder='URL-адресс',
                custom_id='thumbnail',
                style=TextInputStyle.paragraph,
                max_length=500,
            ),
            disnake.ui.TextInput(
                label='image',
                placeholder='URL-адресс',
                custom_id='image',
                style=TextInputStyle.paragraph,
                max_length=500
            ),
            disnake.ui.TextInput(
                label='color embed',
                placeholder='#000000',
                custom_id='color embed',
                style=TextInputStyle.short,
                max_length=7
            )
        ]
        super().__init__(title='Set greeting decoration', components=components)

        self.session = db_session.create_session()
        self.inter = inter

    async def callback(self, inter: disnake.ModalInteraction):
        greeting = self.session.query(checking.Greeting).filter(checking.Greeting.id == 2).first()

        for key, value in inter.text_values.items():
            true_key = '_'.join(key.split())
            if value.lower() == '-':
                exec(f'greeting.{true_key} = None')
            elif value.lower() == 'same':
                pass
            else:
                exec(f'greeting.{true_key} = "{value}"')
        self.session.commit()

        embed = functions.get_greeting_embed(greeting, self.inter, False)

        await self.inter.edit_original_message(embed=embed)
        await inter.send('Информация внесена', delete_after=2)


class ModalAgreementInformation(disnake.ui.Modal):
    def __init__(self, inter):
        components = [
            disnake.ui.TextInput(
                label='description',
                placeholder='URL-адресс',
                custom_id='thumbnail',
                style=TextInputStyle.paragraph,
                max_length=500,
            ),
            disnake.ui.TextInput(
                label='color embed',
                placeholder='#000000',
                custom_id='color embed',
                style=TextInputStyle.short,
                max_length=7
            )
        ]
        super().__init__(title='Set greeting decoration', components=components)

        self.session = db_session.create_session()
        self.inter = inter

    async def callback(self, inter: disnake.ModalInteraction):
        greeting = self.session.query(checking.Greeting).filter(checking.Greeting.id == 2).first()

        for key, value in inter.text_values.items():
            true_key = '_'.join(key.split())
            if value.lower() == '-':
                exec(f'greeting.{true_key} = None')
            elif value.lower() == 'same':
                pass
            else:
                exec(f'greeting.{true_key} = "{value}"')
        self.session.commit()

        embed = functions.get_greeting_embed(greeting, self.inter, False)

        await self.inter.edit_original_message(embed=embed)
        await inter.send('Информация внесена', delete_after=2)