from typing import Optional

from discord.ui import View

from bot.buttons import ButtonCreateChar, ButtonDeleteChar, SelectCharacter


class UserView(View):

    def __init__(self, characters: Optional[list] = None):
        super().__init__()
        if characters:
            select = SelectCharacter(characters)
            self.add_item(select)

        button1 = ButtonCreateChar()
        button2 = ButtonDeleteChar()

        self.add_item(button1)
        self.add_item(button2)
