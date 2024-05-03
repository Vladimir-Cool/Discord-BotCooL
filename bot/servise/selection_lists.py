from typing import List

from discord import Interaction
from discord.app_commands import command, Choice, autocomplete

from api.character_api import CharacterAPIClient


async def name_autocomplete(
    interaction: Interaction, current: str
) -> List[Choice[str]]:
    """
    Запрашивает список персонажей и возвращает список имен
    '-' на каждую проверку 1 АПИ запрос, надо как то сохранять список
    """

    async with CharacterAPIClient() as api_client:
        chars = await api_client.get_char_for_user(discord_id=interaction.user.id)

    return [
        Choice(name=char["name"], value=char["name"])
        for char in chars
        if current.lower() in char["name"].lower()
    ]
