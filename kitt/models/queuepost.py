from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

def load(bot):
    class QueuePost(bot.Base):
        __tablename__ = "queue_posts"

        id: Mapped[int] = mapped_column(primary_key=True)
        creator_id: Mapped[int]
        channel_id: Mapped[int]
        scheduled_time: Mapped[Optional[datetime]]
        is_posted: Mapped[bool]
        message_contents: Mapped[str]

    bot.tables['queueposts'] = QueuePost

def unload(bot):
    pass
