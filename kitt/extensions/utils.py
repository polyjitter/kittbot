from datetime import datetime
import time

import datefinder
from hikari import Embed
from hikari.commands import CommandChoice
import lightbulb
from lightbulb import SlashCommand, Context

utils = lightbulb.Plugin("Utilities")


@utils.command
@lightbulb.option("format", "Format for the timestamp.", choices=[
    CommandChoice(name="Relative Time (x seconds ago)", value="R"),
    CommandChoice(name="Long Date (Month XX, XXXX)", value="D"),
    CommandChoice(name="Short Date (XX/XX/XXXX)", value="d"),
    CommandChoice(name="Long Time (XX:XX:XX AM/PM)", value="T"),
    CommandChoice(name="Long Date/Time (Day, Month XX, XXXX XX:XX:XX AM/PM)", value="F"),
    CommandChoice(name="Short Date/Time (Month XX, XXXX AM/PM)", value="f"),
])
@lightbulb.option("time", "Time to create a timestamp for (Optional)", required=False)
@lightbulb.command("timestamp", "Get a timestamp in Discord format.", ephemeral=True)
@lightbulb.implements(SlashCommand)
async def timestamp(ctx: Context) -> None:
    """Gets the user's locale and makes a timestamp out of the time"""
    times_raw = []
    body = "## Timestamp Creation\nWhen posted to Discord, this timestamp will adjust to the viewer's timezone.\n\n"
    embed = Embed()

    if ctx.options.time:
        for t in datefinder.find_dates(ctx.options.time):
            times_raw.append(t)
    else:
        times_raw.append(datetime.now())

    if ctx.options.format:
        time_fmt = ctx.options.format
    else:
        time_fmt = "t"

    times_converted = [int(time.mktime(t.timetuple())) for t in times_raw]

    if times_converted:
        body += "\n".join(f"`<t:{t}:{time_fmt}>`" for t in times_converted)
        await ctx.respond(body)
    else:
        body = "## Timestamp Creation Failed\nNo time could be extracted from the time you provided."
        await ctx.respond(body)

def load(bot):
    bot.add_plugin(utils)


def unload(bot):
    bot.remove_plugin(utils)
