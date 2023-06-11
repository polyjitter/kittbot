from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

def load(bot):
    class Settings(bot.Base):
        __tablename__ = "settings"

        id: Mapped[str] = mapped_column(primary_key=True)
        value: Mapped[str]

    bot.tables.Settings = Settings

def unload(bot):
    pass
