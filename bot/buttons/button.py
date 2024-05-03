from typing import Any

from discord.ui import Button
from discord import Interaction, ButtonStyle

from bot.modals.character_modal import CharacterCreateModal, CharacterDeleteModal


class ButtonCreateChar(Button):
    """Создание персонажа"""

    def __init__(self):
        super().__init__()
        self.label = "Создание персонажа"
        self.style = ButtonStyle.primary

    async def callback(self, interaction: Interaction) -> Any:
        await interaction.response.send_modal(CharacterCreateModal())


class ButtonDeleteChar(Button):
    """Удалиь персонажа"""

    def __init__(self):
        super().__init__()
        self.label = "Удалить персонажа"
        self.style = ButtonStyle.danger

    async def callback(self, interaction: Interaction) -> Any:

        await interaction.response.send_modal(CharacterDeleteModal())
