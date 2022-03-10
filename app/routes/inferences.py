from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.db import get_session
from app.pydantinc_models import InferenceCreate, InferenceRead, Inferences

router = APIRouter()


@router.post(
    "/",
    tags=["tags"],
    response_model=InferenceRead,
    status_code=status.HTTP_201_CREATED,
    summary="resume",
)
async def create_movie(
    movie: InferenceCreate, session: AsyncSession = Depends(get_session)
):
    # with Session(db) as session:
    db_inference = Inferences.from_orm(movie)
    session.add(db_inference)
    await session.commit()
    await session.refresh(db_inference)
    return db_inference
