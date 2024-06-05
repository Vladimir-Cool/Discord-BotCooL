from functools import wraps
from typing import Dict
import json

from discord import Interaction, Member, Embed

from api.test_api_embed import EmbedAPIClient


def example(interaction: Interaction, *args, **kwargs) -> Dict:
    pass


async def API_create_embed(name: str) -> Embed:
    """
    Получает по API шаблон Embed-а и создает объект Embed.
    name - имя Embed
    """
    async with EmbedAPIClient() as embed_api:
        data = await embed_api.get_embed(name)

    row_embed1 = data["embed_template"]
    dict_row = json.loads(row_embed1)
    return Embed.from_dict(dict_row)


def create_embed(row_embed1: str):
    print("Create ------Embed -------")
    print(type(row_embed1))
    print(row_embed1)
    # dict_row = json.loads(row_embed1)
    return Embed.from_dict(row_embed1)


def command_custom(func):
    """
    -func - декорируемая функция должна выполнять действие и возвращать данные для ответа в формате словаря.
    -msg-data - Словарь, который передается функции interaction.edit_original_response()
        должен содержать
    """

    @wraps(func)
    async def in_func(interaction: Interaction, *args, **kwargs):
        extras = interaction.command.extras
        msg_data = {}
        # try:
        # await interaction.response.defer(ephemeral=False, thinking=True)

        row_data = await func(interaction, *args, **kwargs)
        print("ROW-DATA---------")
        print(row_data)
        print(row_data.keys())
        if "embed" in row_data.keys():
            msg_data["embed"] = create_embed(row_data["embed"])

        if "content" in row_data.keys():
            msg_data["content"] = row_data["content"]

        if "error" in row_data.keys():
            msg_data["content"] = f"ОШИБКА!!! - {row_data['error']}"
        print("MSG_DATA---------")
        print(msg_data)

        # await interaction.edit_original_response(**msg_data)
        await interaction.response.send_message(**msg_data)

        # except Exception as e:
        #     await interaction.edit_original_response(content=f"Ошибка: {e}")

    return in_func
