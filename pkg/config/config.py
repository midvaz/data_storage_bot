import configparser
from dataclasses import dataclass


@dataclass
class Database:
    user: str
    password: str
    host: str
    database: str
    port: str


@dataclass
class Tg_data:
    token: str


@dataclass
class Config:
    db:        Database
    tg_data:     Tg_data


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        db=Database(**config["db"]),
        tg_data=Tg_data(**config["tg_key"])

    )
