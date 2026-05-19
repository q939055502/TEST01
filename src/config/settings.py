from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    db_url: str = "sqlite:///./test.db"
    app_name: str = "Test API"
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()