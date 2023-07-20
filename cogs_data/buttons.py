import time

import disnake
from typing import Optional

from cogs_data import variables_images, modals, variables

from __functions import functions

from db_data import db_session, checking


class GreetingButtons(disnake.ui.View):

    def __init__(self, author=None):
        super().__init__(timeout=None)
        self.value = Optional[bool]
        self.author = author
        self.session = db_session.create_session()

    @disnake.ui.button(
        label='Information',
        style=disnake.ButtonStyle.primary,
        emoji='❔',
        custom_id='GreetingButtons: Information')
    async def inform(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author:
            await functions.check_available(self, inter)
        else:
            await inter.response.send_modal(modal=modals.ModalGreetingInformation(inter))

    @disnake.ui.button(
        label='Decoration',
        style=disnake.ButtonStyle.primary,
        emoji='🔰',
        custom_id='GreetingButtons: Decoration')
    async def decorate(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author:
            await functions.check_available(self, inter)
        else:
            await inter.response.send_modal(modal=modals.ModalGreetingDecoration(inter))

    @disnake.ui.button(
        label='Confirm',
        style=disnake.ButtonStyle.success,
        emoji='✅',
        custom_id='GreetingButtons: Confirm')
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author:
            await functions.check_available(self, inter)

        else:
            self.remove_item(self.confirm)
            self.remove_item(self.inform)
            self.remove_item(self.decorate)
            self.remove_item(self.cancel)

            greetings = self.session.query(checking.Greeting).all()
            functions.copy_greeting_params(greetings[0], greetings[1])
            self.session.commit()

            embed = disnake.Embed(
                title='Изменения применены',
                color=0x138808
            )
            embed.set_image(url=variables_images.confirm_image)

            await inter.response.edit_message(embed=embed, view=self)
            await inter.delete_original_message(delay=5)

    @disnake.ui.button(
        label='Cancel',
        style=disnake.ButtonStyle.danger,
        emoji='❌',
        custom_id='GreetingButtons: Cancel')
    async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        if self.author != inter.author:
            await functions.check_available(self, inter)
        else:
            self.remove_item(self.confirm)
            self.remove_item(self.inform)
            self.remove_item(self.decorate)
            self.remove_item(self.cancel)

            greetings = self.session.query(checking.Greeting).all()
            functions.copy_greeting_params(greetings[1], greetings[0])
            self.session.commit()

            embed = disnake.Embed(
                title='Изменения отменены',
                color=0xff0000
            )
            embed.set_image(url=variables_images.cancel_image)

            await inter.response.edit_message(embed=embed, view=self)
            await inter.delete_original_message(delay=5)
