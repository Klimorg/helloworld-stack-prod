from datetime import date, time, datetime

import arrow
from pydantic import BaseModel, Field, BaseSettings


class InferenceBase(BaseModel):
    inference_date: date = Field(default=arrow.now().format("YYYY-MM-DD"))
    inference_time: time = Field(default=arrow.now().format("HH:mm:ss"))
    num_detections: int = Field(nullable=True)
    confidence: float = Field(ge=0.0, le=1.0)


class Inferences(InferenceBase):
    id: int = Field(default=None, primary_key=True)


class InferenceCreate(InferenceBase):
    class Config:
        orm_mode = True


class InferenceRead(InferenceBase):
    id: int


class DeploymentSettings(BaseSettings):
    deployment_commit: str = Field(env="DEPLOYMENT_COMMIT")
    deployment_date: datetime = Field(env="DEPLOYMENT_DATE")


class DeploymentInfo(BaseModel):
    deployment_commit: str
    deployment_date: datetime
