from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    bot_token: SecretStr
    db_url: SecretStr
    db_database: SecretStr
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

bot_config = BotConfig()


class Emoji:
    """Эмодзи"""

    OK = "✅"
    NO = "❌"
    ASK = "❓"
    WARNING = "⚠️"
    ERROR = "⛔️"
    SETTINGS = "⚙️"
