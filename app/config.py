from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: Literal['dev', 'prod'] = 'dev'
    BLED_CHAT_ID: int
    BOT_TOKEN: SecretStr

    OPENAI_API_MODEL: str
    OPENAI_API_KEY: SecretStr
    OPENAI_API_BASE_URL: str
    OPENAI_CHAT_CONTEXT: str

    SENTRY_DSN: SecretStr
    SENTRY_TRACES_RATE: float
    SENTRY_PROFILES_RATE: float

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
