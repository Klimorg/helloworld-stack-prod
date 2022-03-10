from app.db import init_db
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
async def on_startup():
    await init_db()
    logger.info("DB Init Done")


@app.get("/")
def read_main():
    return {"Hello world"}


@app.get("/healthcheck")
def get_api_status():
    return {"Status": "ok"}
