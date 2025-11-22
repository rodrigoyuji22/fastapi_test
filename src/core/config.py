from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PWD: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file = Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding = "utf-8",
    )

settings = Settings()

# model_config é palavra reservada do BaseSettings, precisa passar dessa forma para funcionar