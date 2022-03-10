from datetime import date, time

from sqlmodel import Field, SQLModel


class InferenceBase(SQLModel):
    inference_date: date
    inference_time: time
    num_detections: int = Field(nullable=True)
    confidence: float = Field(ge=0.0, le=1.0)


class Inferences(InferenceBase, table=True):
    id: int = Field(default=None, primary_key=True)


class InferenceCreate(InferenceBase):
    pass


class InferenceRead(InferenceBase):
    id: int
