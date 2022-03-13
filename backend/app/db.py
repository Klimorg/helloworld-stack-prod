from datetime import date

import databases
import sqlalchemy
from ormar import Date, Float, Integer, Model, ModelMeta, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .config import settings

database = databases.Database(settings.async_db_uri)
metadata = sqlalchemy.MetaData()


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
    num_detections: int = Integer(minimum=0)
    confidence: float = Float(minimum=0, maximum=1)


class Healthcheck(Model):
    class Meta(MainMeta):
        tablename = "healthcheck"

    id: int = Integer(primary_key=True)
    status: str = String(max_length=5)


# engine = sqlalchemy.create_engine(settings.async_db_uri)
engine = create_async_engine(settings.async_db_uri, future=True, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# metadata.create_all


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
