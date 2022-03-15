from datetime import date

from pydantic import BaseModel, Field


class InferenceBase(BaseModel):
    inference_date: date
    num_detections: int = Field(nullable=True)
    confidence: float = Field(ge=0.0, le=1.0)


class Inferences(InferenceBase):
    id: int = Field(default=None, primary_key=True)


class InferenceCreate(InferenceBase):
    class Config:
        orm_mode = True


class InferenceRead(InferenceBase):
    id: int
