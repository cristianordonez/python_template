"""Base Model will be pydantic class that grabs default values from environment or config.ini"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict, YamlConfigSettingsSource


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        yaml_file="config.yaml",
        case_sensitive=False,
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (
            init_settings,  # CLI overrides
            env_settings,  # Environment variables
            dotenv_settings,  # .env
            YamlConfigSettingsSource(settings_cls),  # config.yaml
            file_secret_settings,  # Docker/K8s secrets
        )
