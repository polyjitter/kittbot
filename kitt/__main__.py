import os

import miru
from lightbulb.ext import tasks

from kitt.botapp import BotApp

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

bot = BotApp()

miru.install(bot)
tasks.load(bot)

bot.run()
