from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mathieu's Stack",
    description="""FastAPI, Docker, Uptime-Kuma, Traefik, Postgre stack.""",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_main():
    return {"Hello world"}


@app.get("/healthcheck")
def get_api_status():
    return {"Status": "ok"}
