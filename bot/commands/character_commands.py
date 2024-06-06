from typing import List

from discord import Interaction, Member, Embed
from discord.interactions import InteractionResponse
from discord.app_commands import command, Choice, autocomplete
from discord.ui import View as DiscordView, Select
from discord.components import SelectOption

from api.character_api import CharacterAPIClient
from api.embed_api import EmbedAPIClient
from bot.embeds.character_embed import CharacterEmbed
from bot.embeds.errors_embed import ErrorEmbed
from bot.servise.selection_lists import name_autocomplete
from bot.commands.base import command_custom


# @command(name="персонаж-создать", description="Команда для создания персонажа")
@command_custom
async def character_create(interaction: Interaction, name: str):

    async with CharacterAPIClient() as api_client:
        character = await api_client.post_char(interaction.user.id, name)

    # embed_name = interaction.command.extras.get("embed_name")
    # if embed_name:
    #     async with EmbedAPIClient() as api_embed:
    #         character["embed_name"] = embed_name
    #         embed_raw = await api_embed.render_embed(character)

    # embed = CharacterEmbed(char)
    # await interaction.response.send_message(embed=embed)
    return {"data_obj": character}


# @command(name="персонаж-профиль", description="Команда для просмотра профиля персонажа")
# @autocomplete(name=name_autocomplete)
# async def character_info(interaction: Interaction, name: str):
#     """Просмотр персонажа"""
#     async with CharacterAPIClient() as api_client:
#         characters = await api_client.get_char(
#             interaction.user.id,
#             name,
#         )
#     if characters:
#         embed = CharacterEmbed(characters[0])
#     else:
#         embed = ErrorEmbed(name)
#     return await interaction.response.send_message(embed=embed)


@command_custom
@autocomplete(name=name_autocomplete)
async def character_info(interaction: Interaction, name: str):
    """Просмотр персонажа"""

    async with CharacterAPIClient() as api_client:
        characters = await api_client.get_char(
            interaction.user.id,
            name,
        )

    # embed_name = interaction.command.extras.get("embed_name")
    # if embed_name:
    #     async with EmbedAPIClient() as api_embed:
    #         characters["embed_name"] = embed_name
    #         embed_raw = await api_embed.render_embed(characters)

    return {"data_obj": characters}


@command(name="персонаж-удалить", description="Команда для удаления персонажа")
async def character_delete(interaction: Interaction):
    pass
