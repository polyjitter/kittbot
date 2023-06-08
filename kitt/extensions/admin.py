import lightbulb
from hikari import OptionType
from lightbulb import checks

from kitt.config import Config

admin = lightbulb.Plugin("Admin")

@admin.command
@lightbulb.command("postas", f"Post a message as {Config.BOTNAME}")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def postas(ctx: lightbulb.Context) -> None:
    return

@postas.child
@lightbulb.command("new", f"Creates a new message as {Config.BOTNAME}")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def new(ctx: lightbulb.Context) -> None:
    ...

def load(bot):
    bot.add_plugin(admin)

def unload(bot):
    bot.remove_plugin(admin)