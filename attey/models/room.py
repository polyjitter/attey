from attey.models import options
from attey.models.abc import Model


class RoomModel(Model):
    def __init__(
        self,
        id: int = None,
        name: str = "Unknown Room",
        players: list[str] = [""],
        mic: options.Mic = options.Mic.AVAILABLE,
        nsfw: options.NSFW = options.NSFW.NO,
        visibility: options.Visibility = options.Visibility.PRIVATE,
    ) -> None:
        super().__init__()

        self.id = id
        self.name = name
        self.players = players

        self.mic = mic
        self.nsfw = nsfw
        self.visibility = visibility
