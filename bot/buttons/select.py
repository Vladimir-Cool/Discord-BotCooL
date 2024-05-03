from typing import Optional, List

from discord import Interaction
from discord.ui import Select
from discord.components import SelectOption

from api.character_api import CharacterAPIClient
from bot.embeds.character_embed import CharacterEmbed


class SelectCharacter(Select):
    """Окно выбора персонажей определенного пользователя по id user"""

    def __init__(self, characters: Optional[List] = None):
        super().__init__()
        self.placeholder = "Выберите персонажа"
        if characters:
            for char in characters:
                self.options.append(SelectOption(label=char["name"]))

    async def callback(self, interaction: Interaction):
        async with CharacterAPIClient() as api_client:
            characters = await api_client.get_char(
                interaction.user.id, interaction.data["values"][0]
            )

            embed = CharacterEmbed(characters[0])
            return await interaction.response.send_message(embed=embed)

    @classmethod
    async def select_fabric(cls, discord_id: int) -> Select:
        """
        Создает экземпляр класса.
        Метод нужен поскольку список персонажей получаем асинхронно из бэка
        """
        async with CharacterAPIClient() as api_client:
            raw_list: list = await api_client.get_char_for_user(discord_id=discord_id)

        new_select = cls()
        for el in raw_list:
            new_select.options.append(SelectOption(label=el["name"]))
        print(new_select.type)
        return new_select
