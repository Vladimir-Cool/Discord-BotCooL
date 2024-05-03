from discord import Interaction, Embed
from discord.ui import Modal, TextInput

from api.character_api import CharacterAPIClient
from bot.embeds.character_embed import CharacterEmbed


class CharacterCreateModal(Modal):

    def __init__(self):
        super().__init__(title="Создание нового персонажа")

        row1 = TextInput(
            label="Name",
            placeholder="Enter new characters name...",
            custom_id="name",
            max_length=25,
        )

        self.add_item(row1)

    async def on_submit(self, interaction: Interaction):
        name = self.children[0].value

        async with CharacterAPIClient() as api_client:
            char = await api_client.post_char(interaction.user.id, name)

        embed = CharacterEmbed(char)
        await interaction.response.send_message(embed=embed)


class CharacterDeleteModal(Modal):
    """Проверка перед удалением персонажа"""

    def __init__(self):
        super().__init__(title="Удаление персонажа")

        row1 = TextInput(
            label="Name",
            placeholder="Enter delete characters name...",
            custom_id="name",
            max_length=25,
        )

        self.add_item(row1)

    async def on_submit(self, interaction: Interaction):
        name = self.children[0].value

        async with CharacterAPIClient() as api_client:
            delete_result = await api_client.delete_char(name)

        await interaction.response.send_message(delete_result)

    # @classmethod
    # async def modal_fabric(cls, discord_id: int) -> Modal:
    #     new_modal = cls()
    #     select = await SelectCharacter.select_fabric(discord_id=discord_id)
    #     new_modal.add_item(select)
    #     return new_modal
