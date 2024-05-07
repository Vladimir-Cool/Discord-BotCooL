from discord.app_commands import CommandTree, Command

from api.command_api import CommandsAPIClient
from conf_bot import settings
from base_bot import bot
from commands.info import info
from commands.help import help_func
from commands.user_commands import registration, user_info, user_del
from commands.character_commands import character_info
from commands.test_command import test_one, test_two, test_three


handlers = {
    "test_one": test_one,
    "test_two": test_two,
    "test_three": test_three,
}


command_tree = CommandTree(client=bot)
command_tree.add_command(registration)
command_tree.add_command(user_info)
command_tree.add_command(user_del)
command_tree.add_command(character_info)


async def refresh_commands():

    async with CommandsAPIClient() as command_api:
        command_list = command_api.get_commands()


command_tree.add_command(test_one)
command_tree.add_command(test_two)
command_tree.add_command(test_three)
# bot.tree.add_command(info)
# bot.tree.add_command(help_func)

# bot.tree.add_command(registration)
# bot.tree.add_command(user_info)
# bot.tree.add_command(user_del)
# bot.tree.add_command(character_info)
# bot.tree.add_command(test_one)
# bot.tree.add_command(test_two)
# bot.tree.add_command(test_tree)


bot.run(settings.TOKEN)
