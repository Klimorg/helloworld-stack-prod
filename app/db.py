from datetime import date, time

import databases
import sqlalchemy
from ormar import Date, Float, Integer, Model, ModelMeta, String, Time
from pydantic import PostgresDsn
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

async_db_uri: str = PostgresDsn.build(
    scheme="postgresql+asyncpg",
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    port=str(settings.POSTGRES_PORT),
    path=f"/{settings.POSTGRES_DB}",
)


engine = create_async_engine(async_db_uri, future=True, echo=False)
metadata = sqlalchemy.MetaData()
database = databases.Database(async_db_uri)

# metadata = sqlalchemy.MetaData()
# database = databases.Database("sqlite:///test.db")
# engine = create_engine(database, echo=True)


# You need to subclass your MainMeta class in each Model class as those classes store
# configuration variables that otherwise would be overwritten by each Model.
class MainMeta(ModelMeta):
    metadata = metadata
    database = database


class Inferences(Model):
    class Meta(MainMeta):
        tablename = "inferences"

    id: int = Integer(primary_key=True)
    inference_date: date = Date()
    inference_time: time = Time()
    num_detections: int = Integer(minimum=0)  # type: ignore
    confidence: float = Float(minimum=0, maximum=1)


class Healthcheck(Model):
    class Meta(MainMeta):
        tablename = "healthcheck"

    id: int = Integer(primary_key=True)
    status: str = String(max_length=5)


async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
