from typing import Protocol


class CommandBase(Protocol):
    def call_command(self):
        pass

    def get_error(self):
        pass
