from discord import Client, Intents, Object
from discord.member import Member
from discord.app_commands import CommandTree, Command


from bot.conf_bot import settings, handlers_list
from api.command_api import CommandsAPIClient


# vova_cool_guild = Object(id=settings.GUILD_ID)


class BotClient(Client):
    """
    Ранее был наследник класса Bot, но у него уже определен параметр дерево команд.
    По этому перенаследовался от Client. и пришлось немного изменить код...
    """

    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents().all())
        self.tree = CommandTree(client=self)
        self.synced = False

    async def on_ready(self):
        """Функция запускается когда бот успешно запустился."""
        print("--ОР--РЕАДИ--")
        channel = self.get_channel(settings.CHANNEL_BASIC_ID)
        await self.refresh_commands()
        print(f"Бот запущен ")
        await channel.send("Я снова подключился")

    async def setup_hook(self):
        """---"""
        # self.tree.copy_global_to(guild=TEST_GUILD)
        # await self.tree.sync(guild=vova_cool_guild)

        print("--Сетап--ХУК--")

    async def refresh_commands(self):
        """
        command_list - мы получаем json с настройками команд по API
        """
        self.tree.clear_commands(guild=None)

        async with CommandsAPIClient() as command_api:
            command_list = await command_api.get_commands()

        for row_command in command_list:
            if row_command["enabled"]:
                handlers = handlers_list[row_command["name"]]
                new_command = Command(
                    name=row_command["name"],
                    description=row_command["description"],
                    callback=handlers,
                )
                # new_command.guild_only = True
                # new_command.on_error =
                # new_command.default_permissions =

                self.tree.add_command(new_command)

        result_sync = await self.tree.sync(guild=None)
        print(f"Синхронизировано {len(result_sync)} команд")

    async def on_member_join(self, member: Member = None):
        print(f"новый пользователь")
        channel = self.get_channel(settings.CHANNEL_BASIC_ID)
        await channel.send(f"Добрый день, {member.mention}")

    async def on_member_remove(self, member: Member = None):
        pass

    # async def on_message(self, message: Message, /) -> None:
    #     member: Member = message.author
    #     await self.process_commands(message)


bot = BotClient()
bot.run(settings.TOKEN)
