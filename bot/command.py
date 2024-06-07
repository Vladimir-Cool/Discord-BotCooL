# from discord.app_commands import CommandTree, Command
#
# from api.command_api import CommandsAPIClient
# from bot.conf_bot import settings
# from base_bot import bot

# from commands.info import info
# from commands.help import help_func
# from commands.user_commands import registration, user_info, user_del
# from commands.character_commands import character_info
# from commands.test_command import test_one, test_two, test_three


# handlers_list = {
#     "test_one": test_one,
#     "test_two": test_two,
#     "test_three": test_three,
# }


# async def refresh_commands():
#
#     async with CommandsAPIClient() as command_api:
#         command_list = await command_api.get_commands()
#
#         for raw_command in command_list:
#             if raw_command["enabled"]:
#                 handlers = handlers_list[raw_command["embed"]["name"]]
#                 new_command = Command(
#                     name=raw_command["name"],
#                     description=raw_command["description"],
#                     callback=handlers,
#                 )
#                 new_command.guild_only = True
#                 # new_command.on_error =
#                 # new_command.default_permissions =
#
#                 bot.tree.add_command(new_command)
#
#         bot.tree.sync(guild=vova_cool_guild)


# command_tree = CommandTree(client=bot)
# command_tree.clear_commands(guild=vova_cool_guild)

# bot.tree.add_command(registration)
# bot.tree.add_command(user_info)
# bot.tree.add_command(user_del)
# bot.tree.add_command(character_info)


# bot.tree.add_command(
#     Command(name="refresh", description="рефреш команд", callback=)
# )


# command_tree.add_command(test_two)
# command_tree.add_command(test_three)

# bot.tree.add_command(info)
# bot.tree.add_command(help_func)

# bot.tree.add_command(registration)
# bot.tree.add_command(user_info)
# bot.tree.add_command(user_del)
# bot.tree.add_command(character_info)
# bot.tree.add_command(test_one)
# bot.tree.add_command(test_two)
# bot.tree.add_command(test_tree)


# bot.run(settings.TOKEN)
