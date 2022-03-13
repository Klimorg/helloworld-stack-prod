from typing import Any, Dict, List, Optional, Union

from loguru import logger
from pydantic import BaseSettings, Field, PostgresDsn, validator


class Settings(BaseSettings):
    db_user: str = Field(default="postgres", env="DB_USER")
    db_pwd: str = Field(default="postgres", env="DB_PASSWORD")
    db_host: str = Field(default="db", env="DB_HOST")
    db_port: str = Field(..., env="DB_PORT")
    db_name: str = Field(default="postgres", env="DB_NAME")
    async_db_uri: str = Field(..., env="DATABASE_URL")

    # async_db_uri: Any = (
    #     f"postgresql+asyncpg://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"
    # )

    # @validator("async_db_uri", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     if isinstance(v, (str, int)):
    #         return v
    #     return PostgresDsn.build(
    #         scheme="postgresql+asyncpg",
    #         user=values.get("DB_USER"),
    #         password=values.get("DB_PASSWORD"),
    #         host=values.get("DB_HOST"),
    #         port=values.get("DB_PORT"),
    #         path=f"/{values.get('DB_NAME') or ''}",
    #     )


settings = Settings()
# logger.info(
#     f"async db uri : postgresql+asyncpg://{settings.db_user}:{settings.db_pwd}@{settings.db_host}:5432/{settings.db_name}"
# )

db_uri = PostgresDsn.build(
    scheme="postgresql+asyncpg",
    user=settings.db_user,
    password=settings.db_pwd,
    host=settings.db_host,
    port=settings.db_port,
    path=f"/{settings.db_name or ''}",
)
logger.info(f"db_uri : {db_uri}")
