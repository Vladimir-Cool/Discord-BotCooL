from discord import Interaction

from discord.app_commands import command, Command


@command(name="инфо", description="Тестовая команда для просмотра информации")
async def info(interaction: Interaction):
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")
