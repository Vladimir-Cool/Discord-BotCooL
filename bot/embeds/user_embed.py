from discord import Embed
from typing import Dict


class UserEmbed(Embed):
    def __init__(self, data: Dict):
        super().__init__()
        self.colour = 0x9932CC

        self.title = f"Информация по профилю: {data['name']}"
        self.description = f"Ваш опыт: {data['experience']}%\nКоличество персонажей: {len(data['characters'])} из {data['characters_count']}\n"

        if data["characters"]:
            for char in data["characters"]:
                self.add_field(
                    name=f"Имя: {char['name']}",
                    value=f"Уровень: {char['level']}({char['experience']})",
                )
