import hikari
import lightbulb
import sqlalchemy
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from hikari import Intents, Status, Activity, ActivityType

from kitt import config


class BotApp(lightbulb.BotApp):
    def __init__(self) -> None:
        self.db = create_async_engine(
            f"sqlite+aiosqlite:///{config.DB_FILE}", echo=True, future=True
        )

        self.db_session = async_sessionmaker(self.db, expire_on_commit=False)

        class Base(AsyncAttrs, DeclarativeBase):
            pass

        self.Base = Base

        super().__init__(
            token=config.TOKEN,
            intents=Intents.ALL,
            default_enabled_guilds=(config.HOME_ID),
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
        # TODO replace with logging
        print("Running setup...")

        print("Loading extensions...")
        self.load_extensions_from("./kitt/extensions")

        print("Loading models...")
        self.load_extensions_from("./kitt/models")

        print("Creating tables...")
        async with self.db.begin() as conn:
            await conn.run_sync(self.Base.metadata.create_all)

        print("Setup complete.")
