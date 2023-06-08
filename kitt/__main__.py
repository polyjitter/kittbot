import os
from typing import Final

import hikari
import lightbulb
import miru
from hikari import Intents, Status, Activity, ActivityType
from lightbulb import checks
from lightbulb.ext import tasks

from kitt.config import Config

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()


class KittBotApp(lightbulb.BotApp):
    def __init__(self) -> None:
        super().__init__(
            token=Config.TOKEN,
            intents=Intents.ALL,
            default_enabled_guilds=(Config.HOME_ID),
        )

    def run(self) -> None:
        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)
        # self.event_manager.subscribe(hikari.StartedEvent, self.on_started)
        # self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)

        super().run(
            activity=Activity(type=ActivityType.WATCHING, name="these streets..."),
            status=Status.ONLINE,
        )

    async def on_starting(self, event: hikari.StartingEvent) -> None:
        print("Running setup...")

        print("Loading extensions...")
        self.load_extensions_from("./kitt/extensions")
        print("Extensions loaded.")

        print("Setup complete.")


bot = KittBotApp()

miru.install(bot)
tasks.load(bot)

bot.run()
