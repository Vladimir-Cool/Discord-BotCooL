from discord import Client, Intents
from discord.ext.commands import Bot, command
from discord.ext.commands.context import Context
from discord.message import Message
from discord.member import Member
from discord.app_commands import CommandTree
import discord
from conf_bot import settings

vova_cool_guild = discord.Object(id=settings.GUILD_ID)


class BotClient(Client):
    """
    Ранее был наследник класса Bot, но у него уже определен параметр дерево команд.
    По этому перенаследовался от Client. и пришлось немного изменить код...
    """

    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents().all())
        self.synced = False

    async def on_ready(self):
        """Функция запускается когда бот успешно запустился."""
        print(f"Бот запущен ")
        # await self.tree.sync()

        channel = self.get_channel(settings.CHANNEL_BASIC_ID)
        await channel.send("Я снова подключился")

    # async def setup_hook(self):
    #     """Синхронизирует дерево команд с guild discord"""
    #     # self.tree.copy_global_to(guild=TEST_GUILD)
    #     await self.tree.sync(guild=vova_cool_guild)

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
