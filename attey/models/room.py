from enum import Enum
from typing import Optional

import hikari
import attey

from attey.models import options
from attey.models.abc import Model
from models.player import PlayerModel
from models.channel import ChannelModel
from models.panel import PanelModel


class Mic(Enum):
    DISABLED = 1
    AVAILABLE = 2
    REQUIRED = 3


class Visibility(Enum):
    PRIVATE = 1
    ASK_TO_JOIN = 2
    LOOKING_FOR_GAME = 3


class RoomModel(Model):
    def __init__(
        self,
        id: int = 0,  # 0 = Improper Setup
        name: str = "Unknown Room",
        owner: Optional[PlayerModel] = None,
        players: list[PlayerModel] = [],
        panel: Optional[PanelModel] = None,
        channels: list[ChannelModel] = [],
        mic: Mic = Mic.AVAILABLE,
        nsfw: bool = False,
        visibility: Visibility = Visibility.PRIVATE,
    ) -> None:
        super().__init__(id)

        self.name = name
        self.owner = owner

        self.players = players
        self.panel = panel
        self.channels = channels

        self.mic = mic
        self.nsfw = nsfw
        self.visibility = visibility

    async def init_room(
        self,
        guild: hikari.Guild = attey.HOME,
    ) -> hikari.GuildCategory:
        category = await guild.create_category(name=self.name)
        self.id = category.id
        await self.save()  # Save to the database to avoid issues

        panel_channel = guild.create_text_channel(
            "panel",
            nsfw=self.nsfw,
            category=category,
        )
        self.panel = PanelModel(panel_channel.id)

        

    async def save(self):
        ...
