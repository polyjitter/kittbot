import lightbulb
import sqlalchemy

admin = lightbulb.Plugin("Admin")


def load(bot):
    bot.add_plugin(admin)


def unload(bot):
    bot.remove_plugin(admin)
