import rethinkdb
import toml

with open("./pyproject.toml") as f:
    _poetry = toml.load(f)

    __version__ = _poetry["tool"]["poetry"]["version"]

with open("./config.toml") as f:
    _config = toml.load(f)

    # __authors__ = _config["AUTHORS"]

    TOKEN = _config["bot"]["token"]
    MAINTENANCE = _config["bot"]["maintenance"]
    HOME_GUILD = _config["bot"]["home_guild"]

    if _config["rethink"]["name"]:
        re = rethinkdb.RethinkDB()
        re.set_loop_type("asyncio")
        DB_NAME = _config["rethink"]["name"]
        DB_TABLES = _config["rethink"]["tables"]
