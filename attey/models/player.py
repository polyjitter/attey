import hikari

from attey.models.abc import Model

class PlayerModel(Model):
    def __init__(self, id: int = None) -> None:
        super.__init__(id)