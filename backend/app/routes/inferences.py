from fastapi import APIRouter, status
from sqlmodel import select

from ..db import Inferences
from ..pydantinc_models import InferenceCreate, InferenceRead

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
