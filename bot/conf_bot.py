from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings
from commands.test_command import test_one, test_two, test_three
from commands.refresh import refresh_com

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
}
