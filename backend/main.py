from app.db import Inferences, database
from app.routes import inferences
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

app = FastAPI(
    title="Mathieu's Stack",
    description="""FastAPI, Docker, Uptime-Kuma, Traefik, Postgre stack.""",
    version="0.1.0",
)

app.include_router(inferences.router, prefix="/inferences")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.get("/")
def read_main():
    return {"Hello world"}


@app.get("/healthcheck")
def get_api_status():
    return {"Status": "ok"}
