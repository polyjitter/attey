from enum import Enum

import hikari

from attey.models.abc import Model

class ChannelType(Enum):
    OFFTOPIC = 1
    ALL_PLAYERS = 2
    TEAM = 3
    PLAYER = 4

class ChannelModel(Model):
    def __init__(self, id: int, type: ChannelType) -> None:
        super.__init__(id)

        self.type = type