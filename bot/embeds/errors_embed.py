from discord import Embed


class ErrorEmbed(Embed):
    def __init__(self, name: str):
        super().__init__()
        self.colour = 0xFF0000

        self.title = f"Персонажа {name} нет"
        self.description = f"Ой йой йоой"
