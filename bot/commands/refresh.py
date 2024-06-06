from discord import Interaction

from .base import command_custom


@command_custom
async def refresh_com(interaction: Interaction):
    await interaction.client.refresh_commands()
    return {"content": "Готово"}
