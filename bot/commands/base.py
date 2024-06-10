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
        """
        Декоратор для функций команд.
        row_data - словарь который вернет команда. по нему и генерируется ответ.

        embed_name - Имя ембеда прикрепленного к команде. если его нет то в ответе не будет ембеда

        :return:
        """
        msg_data = {}
        # try:
        # await interaction.response.defer(ephemeral=False, thinking=True)

        raw_data = await func(interaction, *args, **kwargs)
        print("RAW-DATA---------")
        print(raw_data)
        print(raw_data.keys())

        if "content" in raw_data.keys():
            msg_data["content"] = raw_data["content"]

        # Тут не явный момент. Имя Embed внутри команды.
        # Какой объект нужен для рендеренги нигде не определено.
        # Это придется помнить.
        embed_name = interaction.command.extras.get("embed_name")
        if embed_name:
            if "data_obj" in raw_data.keys():
                async with EmbedAPIClient() as api_embed:
                    raw_data["data_obj"]["embed_name"] = embed_name
                    embed_raw = await api_embed.render_embed(raw_data["data_obj"])
                msg_data["embed"] = create_embed(embed_raw)

        # if "embed" in raw_data.keys():
        #     msg_data["embed"] = create_embed(raw_data["embed"]

        if "view" in raw_data.keys():
            msg_data["view"] = raw_data["view"]

        if "error" in raw_data.keys():
            msg_data["content"] = f"ОШИБКА!!! - {raw_data['error']}"

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
    Пример функции 'команд' для понимания
    :param **kwarg Можно объявлять любые переменные, в декораторе они все пересылаються

    В функции происходит нужная нам логика.


    :return Возвращаем словарь ключи словаря:
    ---'content' - Сообщение, которое будет передано.
    Просто сообщение которое будет видно над всеми остальными элементами

    ---'data_obj' - Объект для рендеринга Embed.
    Имя embed_name крепиться к команде на стадии обновления команд (оно берется из базы) там же хранится шаблон по которому
    будет собран Embed.

    ПОКА НЕТ ---'embed' - Готовый словарь для класса Embed.

    ---'error' - Сообщение ошибки.

    ---'view' - Готовый объект View. Содержит кнопки и селекты. Все это пока что генерируется в команде.
    """
    pass
    return {}
