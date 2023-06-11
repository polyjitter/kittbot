import lightbulb
from lightbulb.ext import tasks
import sqlalchemy

from kitt import config
from kitt.botapp import BotApp

ikroles = lightbulb.Plugin("Improv Knight Roles")


@tasks.task(m=5, pass_app=True, auto_start=True, wait_before_execution=True)
async def add_to_squire_role(bot: BotApp):
    print("This shit running")

    guild = bot.cache.get_guild(config.HOME_ID)
    members = [m for (_, m) in guild.get_members().items()]

    print(members)

    squire_role_id = 1117317724901756959
    level_roles = [1112693123185922089, 1112693346067025981, 1112694263944319086]

    def member_filter(member):

        roles = member.get_roles()

        role_ids = [r.id for r in roles]

        if any(r in level_roles for r in role_ids):
            f1 = True
        else:
            f1 = False

        if squire_role_id not in role_ids:
            f2 = True
        else:
            f2 = False

        if f1 and f2:
            return True
        else:
            return False

    needed_members = filter(member_filter, members)

    for m in needed_members:
        await m.add_role(squire_role_id)


def load(bot):
    bot.add_plugin(ikroles)


def unload(bot):
    bot.remove_plugin(ikroles)
