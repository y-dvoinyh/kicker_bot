"""This file represents configurations from files and environment."""

import logging
from dataclasses import dataclass
from os import getenv


@dataclass
class BotConfig:
    """Bot configuration."""

    token: str = getenv('BOT_TOKEN')


@dataclass
class RedisConfig:
    """Redis connection variables."""

    db: int = int(getenv('REDIS_DATABASE', 1))
    """ Redis Database ID """
    host: str = getenv('REDIS_HOST', 'localhost')
    port: int = int(getenv('REDIS_PORT', 6379))
    passwd: str | None = getenv('REDIS_PASSWORD')
    username: str | None = getenv('REDIS_USERNAME')
    state_ttl: int | None = getenv('REDIS_TTL_STATE', None)
    data_ttl: int | None = getenv('REDIS_TTL_DATA', None)


@dataclass
class Configuration:
    """All in one configuration's class."""

    debug = bool(getenv('DEBUG'))
    logging_level = int(getenv('LOGGING_LEVEL', logging.INFO))

    bot = BotConfig()
    redis = RedisConfig()


conf = Configuration()
