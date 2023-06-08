import hikari
import lightbulb
import miru
from hikari import ButtonStyle
from hikari.embeds import Embed

from kitt.config import Config
from kitt.components.dialogs import ConfirmationDialog

admin = lightbulb.Plugin("Admin")


@admin.command
@lightbulb.option("message", "Message to post", type=str)
@lightbulb.option("channel", "Channel to post to", type=hikari.TextableGuildChannel)
@lightbulb.command("postas", f"Post a message as {Config.BOTNAME}")
@lightbulb.implements(lightbulb.SlashCommand)
async def postas(ctx: lightbulb.Context) -> None:
    body = "# Post Message?"
    embed = Embed()
    embed.add_field("Channel", ctx.options.channel.mention)
    embed.add_field("Message", ctx.options.message)
    view = ConfirmationDialog()

    response = await ctx.respond(body, embed=embed, components=view)
    msg = await response.message()

    await view.start(msg)
    await view.wait()
    if view.answer is True:
        await ctx.bot.rest.create_message(ctx.options.channel.id, ctx.options.message)
        await response.edit(
            f"**Message posted.** Please check {ctx.options.channel.mention}.",
            embed=None,
            components=None,
        )

    elif view.answer is False:
        await response.edit(
            "**Message cancelled.**",
            embed=None,
            components=None,
        )


def load(bot):
    bot.add_plugin(admin)


def unload(bot):
    bot.remove_plugin(admin)
