from typing import List

from fastapi import APIRouter, status

from app.db import Inferences
from app.pydantic_models import InferenceCreate, InferenceRead

router = APIRouter()


@router.post(
    "/",
    tags=["tags"],
    response_model=InferenceRead,
    status_code=status.HTTP_201_CREATED,
    summary="resume",
)
async def create_inference(inference: InferenceCreate):
    return await Inferences(**inference.dict()).save()


@router.get(
    "/",
    tags=["tags"],
    response_model=List[InferenceRead],
    status_code=status.HTTP_200_OK,
    summary="resume",
)
async def get_inference():
    return await Inferences.objects.all()
