import hikari
import miru

from models.room import RoomModel

class CreationPanelView(miru.View):
    def __init__(
        self,
        *args,
        timeout=120.0,
        autodefer=True,
    ) -> None:
        super().__init__(*args, timeout, autodefer)

        self.model: RoomModel = RoomModel()

    # @miru.select(
    #     placeholder="",
    #     options=[
    #         miru.SelectOption(label="Open")
    #     ]
    # )
