from discord import Embed
from typing import Dict


class CharacterEmbed(Embed):
    def __init__(self, data: Dict):
        super().__init__()
        self.colour = 0x7FFFD4

        self.title = f"Информация по прерсанажу: {data['name']}"
        self.description = f"Уровень: {data['level']}({data['experience']})%\nБольше информации пока нет, но когда нибудь она будет=)"
