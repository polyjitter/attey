import os

import hikari
import lightbulb
import miru
from hikari.api.cache import Cache

import attey


attey.bot = lightbulb.BotApp(
        token=attey.TOKEN,
        intents=(
            hikari.Intents.GUILD_MESSAGES
            | hikari.Intents.GUILD_MESSAGE_REACTIONS
            | hikari.Intents.MESSAGE_CONTENT
            | hikari.Intents.GUILD_WEBHOOKS
        ),
        default_enabled_guilds=attey.HOME_ID,
    )

attey.bot.load_extensions_from("./attey/commands")

miru.load(attey.bot)

@attey.bot.listen()
async def on_connect(event: hikari.events.StartedEvent):
    attey.HOME = Cache.get_available_guild(attey.HOME_ID)

if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

attey.bot.run()