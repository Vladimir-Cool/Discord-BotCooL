from discord import Interaction
from discord.app_commands import command


@command(name="помощь", description="Команда приветствия")
async def help_func(interaction: Interaction):
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")
