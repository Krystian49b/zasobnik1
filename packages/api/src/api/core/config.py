from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application configuration settings.
    """

    # General settings
    app_name: str = Field("MyApp", env="APP_NAME")
    app_version: str = Field("1.0.0", env="APP_VERSION")


@lru_cache()
def get_settings() -> Settings:
    """
    Retrieve application settings, caching the result for performance.
    """
    return Settings()
