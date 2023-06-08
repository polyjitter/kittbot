import lightbulb
import sqlalchemy

admin = lightbulb.Plugin("Admin")

def load(bot):
    bot.db.tables["queue"] = sqlalchemy.Table(
        "queue",
        bot.db.meta,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("creator_id", sqlalchemy.String(length=19)),
        sqlalchemy.Column("channel_id", sqlalchemy.String(length=19)),
        sqlalchemy.Column("scheduled_time", sqlalchemy.DateTime),
        sqlalchemy.Column("is_posted", sqlalchemy.Boolean),
    )
    bot.add_plugin(admin)


def unload(bot):
    bot.remove_plugin(admin)
