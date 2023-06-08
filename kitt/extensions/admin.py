import hikari
import lightbulb
import miru
from hikari import ButtonStyle
from hikari.embeds import Embed

from kitt import config
from kitt.components.dialogs import ConfirmationDialog

admin = lightbulb.Plugin("Admin")


@admin.command
@lightbulb.option("message", "Message to post", type=str)
@lightbulb.option(
    "channel",
    "Channel to post to",
    type=hikari.TextableGuildChannel,
    channel_types=[hikari.ChannelType.GUILD_TEXT],
)
@lightbulb.command("postas", f"Post a message as {config.BOTNAME}")
@lightbulb.implements(lightbulb.SlashCommand)
async def postas(ctx: lightbulb.Context) -> None:
    """Creates a new post as the bot, with a confirmation dialog."""

    body = "# Post Message?"
    embed = Embed()
    embed.add_field("Channel", ctx.options.channel.mention)
    embed.add_field("Message", ctx.options.message)
    view = ConfirmationDialog()

    response = await ctx.respond(body, embed=embed, components=view)
    msg = await response.message()

    await view.start(msg)
    await view.wait()

    match view.answer:
        case True:
            await ctx.bot.rest.create_message(ctx.options.channel.id, ctx.options.message)
            await response.edit(
                f"**Message posted.** Please check {ctx.options.channel.mention}.",
                embed=None,
                components=None,
            )
        case False:
            await response.edit(
                "**Message cancelled.**",
                embed=None,
                components=None,
            )


def load(bot):
    bot.add_plugin(admin)


def unload(bot):
    bot.remove_plugin(admin)
