"""
Configuration management for IntraMind.

Handles environment variables, settings, and configuration validation.
"""

import os
from typing import Any, Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Application configuration.

    All sensitive values should be loaded from environment variables.
    Never hardcode credentials in this file.
    """

    # Application Settings
    app_name: str = Field(default="IntraMind", env="APP_NAME")
    app_env: str = Field(default="development", env="APP_ENV")
    debug: bool = Field(default=False, env="DEBUG")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    # Server Configuration
    host: str = Field(default="0.0.0.0", env="HOST")
    port: int = Field(default=8000, env="PORT")
    workers: int = Field(default=4, env="WORKERS")

    # Database Configuration
    database_url: str = Field(default="postgresql://user:****@localhost:5432/intramind", env="DATABASE_URL")
    database_pool_size: int = Field(default=20, env="DATABASE_POOL_SIZE")

    # Redis Configuration
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    cache_ttl: int = Field(default=3600, env="CACHE_TTL")

    # AI Model Configuration
    ai_provider: str = Field(default="openai", env="AI_PROVIDER")
    openai_api_key: Optional[str] = Field(default="****", env="OPENAI_API_KEY")
    model_name: str = Field(default="gpt-4", env="OPENAI_MODEL")
    temperature: float = Field(default=0.7, env="OPENAI_TEMPERATURE")
    max_tokens: int = Field(default=2000, env="OPENAI_MAX_TOKENS")

    # Security
    secret_key: str = Field(default="****", env="SECRET_KEY")
    jwt_secret: str = Field(default="****", env="JWT_SECRET")
    api_key: Optional[str] = Field(default="****", env="API_KEY")

    # Rate Limiting
    rate_limit_per_minute: int = Field(default=60, env="RATE_LIMIT_PER_MINUTE")
    rate_limit_per_hour: int = Field(default=1000, env="RATE_LIMIT_PER_HOUR")

    @field_validator("app_env")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate that app_env is one of the allowed values."""
        allowed = ["development", "staging", "production"]
        if v not in allowed:
            raise ValueError(f"app_env must be one of {allowed}")
        return v

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate that log_level is valid."""
        allowed = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        v_upper = v.upper()
        if v_upper not in allowed:
            raise ValueError(f"log_level must be one of {allowed}")
        return v_upper

    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global configuration instance
config = Config()
