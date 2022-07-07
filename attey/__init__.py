import json

import rethinkdb

with open("./config.json") as f:
    _config = json.load(f)

    __version__ = _config["VERSION"]
    # __authors__ = _config["AUTHORS"]

    MAINTENANCE = _config["MAINTENANCE"]

    if _config['RETHINK']['DB']:
        re = rethinkdb.RethinkDB()
        re.set_loop_type("asyncio")
        DB_NAME = _config['RETHINK']['NAME']
        DB_TABLES = _config['RETHINK']['TABLES']