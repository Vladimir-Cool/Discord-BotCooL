import json

from discord import Interaction, Member, Embed
from discord.app_commands import command
from discord.ext.commands import Context


from api.user_api import UserAPIClient
from api.base_api import APIException
from bot.embeds.user_embed import UserEmbed
from bot.views.user_view import UserView

row_embed_1 = {
    "title": "Заголовок1",
    "description": "Описание1",
    "color": 16711680,
    "fields": [
        {"name": "Поле 1", "value": "Значение поля 1", "inline": False},
        {"name": "Поле 2", "value": "Значение поля 2", "inline": False},
    ],
}

row_embed_2 = {
    "title": "Заголовок2",
    "description": "Описание2",
    "color": 16711690,
    "fields": [
        {"name": "Поле 1", "value": "Значение поля 1", "inline": True},
        {"name": "Поле 2", "value": "Значение поля 2", "inline": True},
    ],
}

row_embed_3 = {
    "title": "Заголовок3",
    "description": "Описание3",
    "color": 16714249,
    "fields": [
        {"name": "Поле 1", "value": "Значение поля 1", "inline": True},
        {"name": "Поле 2", "value": "Значение поля 2", "inline": True},
        {"name": "Поле 3", "value": "Значение поля 3", "inline": True},
    ],
}

embed_1 = Embed.from_dict(row_embed_1)
embed_2 = Embed.from_dict(row_embed_2)
embed_3 = Embed.from_dict(row_embed_3)


json_example = {
    "content": str(),
    "embed": Embed(),
}


@command(name="test-one", description="Тестирование для фабрики команд 1")
async def test_one(interaction: Interaction, arg: str):
    extras = interaction.extras
    await interaction.response.send_message(f"тест {arg}", embed=embed_1)


@command(name="test-two", description="Тестирование для фабрики команд 2")
async def test_two(interaction: Interaction, arg: str):

    await interaction.response.send_message(f"тест {arg}", embed=embed_2)


@command(name="test-tree", description="Тестирование для фабрики команд 3")
async def test_tree(interaction: Interaction, arg: str):

    await interaction.response.send_message(f"тест {arg}", embed=embed_3)
