from discord import Interaction
from discord.app_commands import command

from bot.commands.base import command_custom
from api.command_api import CommandsAPIClient


# @command(name="помощь", description="Команда приветствия")
# async def help_func(interaction: Interaction):
#     await interaction.response.send_message(f"Hi, {interaction.user.mention}")


@command_custom
async def help_func(interaction: Interaction):
    async with CommandsAPIClient() as api_command:
        command_list = await api_command.get_commands()
    msg = ""
    print(command_list)
    for row in command_list:
        if row["enabled"]:
            msg += f"-\"{row['name']}\": {row['description']} - Embed: \"{row['embed']['name'] if row['embed'] else 'Нету'}\"\n"

    return {"content": msg}
