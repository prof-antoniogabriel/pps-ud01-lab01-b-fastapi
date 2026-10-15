from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "API de avisos de seguridad"
    app_env: str = "development"
    notice_limit: int = 50

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
