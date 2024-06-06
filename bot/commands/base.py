from functools import wraps
from typing import Dict
import json

from discord import Interaction, Member, Embed

from api.embed_api import EmbedAPIClient


def example(interaction: Interaction, *args, **kwargs) -> Dict:
    pass


async def fall__API_create_embed(name: str) -> Embed:
    """
    ПЕРЕПИСАТЬ ПОД РЕНДЕРИНГ
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

        if "content" in row_data.keys():
            msg_data["content"] = row_data["content"]

        embed_name = interaction.command.extras.get("embed_name")
        if embed_name:
            if "data_obj" in row_data.keys():
                async with EmbedAPIClient() as api_embed:
                    row_data["data_obj"]["embed_name"] = embed_name
                    embed_raw = await api_embed.render_embed(row_data["data_obj"])
                msg_data["embed"] = create_embed(embed_raw)

        # if "embed" in row_data.keys():
        #     msg_data["embed"] = create_embed(row_data["embed"]

        if "view" in row_data.keys():
            msg_data["view"] = row_data["view"]

        if "error" in row_data.keys():
            msg_data["content"] = f"ОШИБКА!!! - {row_data['error']}"

        print("MSG_DATA---------")
        print(msg_data)

        # await interaction.edit_original_response(**msg_data)
        await interaction.response.send_message(**msg_data)

        # except Exception as e:
        #     await interaction.edit_original_response(content=f"Ошибка: {e}")

    return in_func


@command_custom
async def example_command(interaction: Interaction):
    """
    Привер функции сомант для понимания
    :param **kwarg Можно объявлять любые переменные, в декораторе они все пересылаються

    В функции происходит нужная нам логика

    :return Возвращаем словарь ключи словаря:
    ---'content' - Сообщение, которое будет передано
    ---'data_obj' - Объект для рендеринга Embed
    ---'embed' - Готовый словарь для класса Embed
    ---'error' - Сообщение ошибки
    ---'view' - Готовый объект View. Содержит кнопки и селекты. Все это пока что генерируется в команде.
    """
    pass
    return {}
