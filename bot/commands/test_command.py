from discord import Interaction

from .base import command_custom
from api.test_api_embed import EmbedAPIClient


@command_custom
async def test_one(interaction: Interaction, arg: str):
    embed = interaction.command.extras.get("embed")

    if embed:
        async with EmbedAPIClient() as api_embed:
            response = await api_embed.get_embed(embed)

        return {
            "content": f"Сказал {arg} а embed команды {embed}",
            "embed": response["embed_template"],
        }


@command_custom
async def test_two(interaction: Interaction, arg: str):
    embed = interaction.command.extras.get("embed")

    if embed:
        async with EmbedAPIClient() as api_embed:
            response = await api_embed.get_embed(embed)

    return {"content": f"Сказал{arg}", "embed": response["embed_template"]}


@command_custom
async def test_three(interaction: Interaction, arg: str):
    return {"content": f"Сказал{arg}", "embed": "embed_3"}
