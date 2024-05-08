from discord import Interaction

from .base import command_custom


# async def refresh_com(interaction: Interaction):
#     await interaction.response.defer(ephemeral=False, thinking=True)
#     await interaction.client.refresh_commands()
#
#     await interaction.edit_original_response(content=f"Готово")
@command_custom
async def refresh_com(interaction: Interaction):
    await interaction.client.refresh_commands()
    return {"content": "Готово"}
