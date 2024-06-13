from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings
from bot.commands.test_command import test_one, test_two, test_three
from bot.commands.refresh import refresh_com
from bot.commands.user_commands import user_info, user_reg, user_del
from bot.commands.help import help_func
from bot.commands.character_commands import (
    character_info,
    character_create,
    character_delete,
)

load_dotenv(dotenv_path="..\.env")


class Setting(BaseSettings):
    TOKEN: str = os.getenv("TOKEN")
    GUILD_ID: str = os.getenv("GUILD_ID")
    CHANNEL_BASIC_ID: int = os.getenv("CHANNEL_BASIC_ID")


settings = Setting()


handlers_list = {
    "test_one": test_one,
    "test_two": test_two,
    "test_three": test_three,
    "refresh_com": refresh_com,
    "user_info": user_info,
    "user_reg": user_reg,
    "help": help_func,
    "char_info": character_info,
    "char_create": character_create,
    "char_delete": character_delete,
    "user_del": user_del,
}
