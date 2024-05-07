from functools import wraps
from typing import Dict

from discord import Interaction


def example(interaction: Interaction, *args, **kwargs) -> Dict:
    pass



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
