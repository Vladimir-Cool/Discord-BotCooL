from discord import Interaction


async def refresh_com(interaction: Interaction):
    await interaction.response.defer(ephemeral=False, thinking=True)
    await interaction.client.refresh_commands()

    await interaction.edit_original_response(content=f"Готово")
