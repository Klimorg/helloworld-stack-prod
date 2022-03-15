from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_user: str = Field(default="postgres", env="DB_USER")
    db_pwd: str = Field(default="postgres", env="DB_PASSWORD")
    db_host: str = Field(default="db", env="DB_HOST")
    db_port: str = Field(default="5432", env="DB_PORT")
    db_name: str = Field(default="postgres", env="DB_NAME")


settings = Settings()
