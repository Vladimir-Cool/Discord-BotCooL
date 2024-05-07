from functools import wraps
from typing import Dict
import json

from discord import Interaction, Member, Embed

from api.test_api_embed import EmbedAPIClient


def example(interaction: Interaction, *args, **kwargs) -> Dict:
    pass


async def create_embed(name: str) -> Embed:
    """
    Получает по API шаблон Embed-а и создает объект Embed.
    name - имя Embed
    """
    async with EmbedAPIClient() as embed_api:
        data = await embed_api.get_embed(name)

    row_embed1 = data["embed_template"]
    dict_row = json.loads(row_embed1)
    return Embed.from_dict(dict_row)


def command_custom(func):
    """
    Деоратор для функций которые будут командами.

    func - декорируемая функция должна выполнять действие и возвращать данные для ответа в формате словаря.

    msg-data - Словарь который передается функции interaction.edit_original_response()
        должен содержать
    """

    @wraps(func)
    async def in_func(interaction: Interaction, *args, **kwargs):
        extras = interaction.command.extras
        await interaction.response.defer(ephemeral=False, thinking=True)

        msg_data = await func(interaction, *args, **kwargs)
        await interaction.edit_original_response(**msg_data)

    return in_func
