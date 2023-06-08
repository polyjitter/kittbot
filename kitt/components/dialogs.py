import miru
from hikari import ButtonStyle


class ConfirmationDialog(miru.View):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @miru.button(label="Cancel", style=ButtonStyle.DANGER)
    async def cancel(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        self.answer = False
        self.stop()

    @miru.button(label="Confirm", style=ButtonStyle.SUCCESS)
    async def confirm(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        self.answer = True
        self.stop()
