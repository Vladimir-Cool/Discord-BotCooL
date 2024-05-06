import json

from discord import Interaction, Member, Embed
from discord.app_commands import command
from discord.ext.commands import Context

from api.test_api_embed import EmbedAPIClient
from bot.embeds.user_embed import UserEmbed
from bot.views.user_view import UserView

# json_example = {
#     "content": str(),
#     "embed": Embed(),
# }

async def create_embed(name: str) -> Embed:
    """
    Получает по API шаблон Embed-а и создает объект Embed.
    """
    async with EmbedAPIClient() as embed_api:
        data = await embed_api.get_embed(name)

    row_embed1 = data["embed_template"]
    dict_row = json.loads(row_embed1)
    return Embed.from_dict(dict_row)


@command(name="test-one", description="Тестирование для фабрики команд 1")
async def test_one(interaction: Interaction, arg: str):
    embed = await create_embed(name="embed_1")

    await interaction.response.send_message(f"тест {arg}", embed=embed)


@command(name="test-two", description="Тестирование для фабрики команд 2")
async def test_two(interaction: Interaction, arg: str):
    embed = await create_embed(name="embed_2")

    await interaction.response.send_message(f"тест {arg}", embed=embed)


@command(name="test-tree", description="Тестирование для фабрики команд 3")
async def test_tree(interaction: Interaction, arg: str):
    embed = await create_embed(name="embed_3")

    await interaction.response.send_message(f"тест {arg}", embed=embed)
