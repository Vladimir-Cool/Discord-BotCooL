from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings


load_dotenv()

class Setting(BaseSettings):
    TOKEN: str = os.getenv("TOKEN")
    GUILD_ID: str = os.getenv("GUILD_ID")
    CHANNEL_BASIC_ID: int = os.getenv("CHANNEL_BASIC_ID")

settings = Setting()

