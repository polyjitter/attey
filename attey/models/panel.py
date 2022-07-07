import hikari

from attey.models.abc import Model

class PanelModel(Model):
    def __init__(self, id: int) -> None:
        super.__init__(id)