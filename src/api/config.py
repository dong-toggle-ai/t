from pydantic import BaseSettings


class Config(BaseSettings):
    # log_level
    LOG_LEVEL: str = "error"


config = Config()
