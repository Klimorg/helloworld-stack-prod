from datetime import date

import databases
import sqlalchemy
from ormar import Date, Float, Integer, Model, String

from .config import settings

database = databases.Database(settings.async_db_uri)
metadata = sqlalchemy.MetaData()


class Inferences(Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "inferences"

    id: int = Integer(primary_key=True)
    inference_date: date = Date()
    num_detections: int = Integer(minimum=0)
    confidence: float = Float(minimum=0, maximum=1)


class Healthcheck(Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "healthcheck"

    id: int = Integer(primary_key=True)
    status: str = String(max_length=5)


engine = sqlalchemy.create_engine(settings.async_db_uri)
metadata.create_all(engine)
