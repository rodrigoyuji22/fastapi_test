from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    def __init__(self, **data):
        super().__init__(**data)

    DB_HOST: str
    DB_USER: str
    DB_PWD: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
