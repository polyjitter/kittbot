from typing import Final

import toml

class Config:
    with open("./pyproject.toml") as f:
        _poetry = toml.load(f)

        VERSION: Final = _poetry["tool"]["poetry"]["version"]

    with open("./config.toml") as f:
        _config = toml.load(f)

        # __authors__ = _config["AUTHORS"]

        TOKEN: Final = _config["bot"]["token"]
        MAINTENANCE: Final = _config["bot"]["maintenance"]
        HOME_ID: Final = _config["bot"]["home_guild"]
        BOTNAME: Final = _config["bot"]["name"]