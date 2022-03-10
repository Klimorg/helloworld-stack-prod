from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, Field, PostgresDsn, validator


class Settings(BaseSettings):
    db_user: str = Field(..., env="DB_USER")
    db_pwd: str = Field(..., env="DB_PASSWORD")
    db_host: str = Field(..., env="DB_HOST")
    db_port: Union[int, str] = Field(..., env="DB_PORT")
    db_name: str = Field(..., env="DB_NAME")

    async_db_uri: Optional[
        Any
    ] = f"postgresql+asyncpg://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"

    @validator("async_db_uri", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, (str, int)):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )


settings = Settings()
