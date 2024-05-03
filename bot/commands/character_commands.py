from typing import List

from discord import Interaction, Member, Embed
from discord.interactions import InteractionResponse
from discord.app_commands import command, Choice, autocomplete
from discord.ui import View as DiscordView, Select
from discord.components import SelectOption

from api.character_api import CharacterAPIClient
from api.base_api import APIException
from bot.embeds.character_embed import CharacterEmbed
from bot.embeds.errors_embed import ErrorEmbed
from bot.servise.selection_lists import name_autocomplete


@command(name="персонаж-создать", description="Команда для создания персонажа")
async def character_create(interaction: Interaction):
    # async with
    pass


@command(name="персонаж-профиль", description="Команда для просмотра профиля персонажа")
@autocomplete(name=name_autocomplete)
async def character_info(interaction: Interaction, name: str):
    """Просмотр персонажа"""
    async with CharacterAPIClient() as api_client:
        characters = await api_client.get_char(
            interaction.user.id,
            name,
        )
    if characters:
        embed = CharacterEmbed(characters[0])
    else:
        embed = ErrorEmbed(name)
    return await interaction.response.send_message(embed=embed)


@command(name="персонаж-удалить", description="Команда для удаления персонажа")
async def character_delete(interaction: Interaction):
    pass
