import os
import json

import hikari
import lightbulb

import attey


def create_bot() -> lightbulb.BotApp:

    with json.load(open("./config.json")) as f:
        token = f["TOKEN"]

    bot = lightbulb.BotApp(
        token=token,
        intents=[
            hikari.Intents.GUILD_MESSAGES,
            hikari.Intents.GUILD_MESSAGE_REACTIONS,
            hikari.Intents.MESSAGE_CONTENT,
            hikari.Intents.GUILD_WEBHOOKS,
        ],
    )

    bot.load_extensions_from("./attey/commands")

    return bot


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    create_bot().run()
