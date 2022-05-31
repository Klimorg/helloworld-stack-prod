# from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.db import Healthcheck, database, init_models
from app.routes import inferences
from app.pydantic_models import DeploymentSettings, DeploymentInfo

app = FastAPI(
    title="Mathieu's Stack",
    description="FastAPI, Docker, Uptime-Kuma, Traefik, Postgre stack.",
    version="0.1.0",
)

app.include_router(inferences.router, prefix="/inferences")

# app.add_middleware(
#     ElasticAPM,
#     client=make_apm_client(
#         {"SERVICE_NAME": "fastapi-app", "SERVER_URL": "http://apm-server:8200"},
#     ),
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    await init_models()
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    await Healthcheck.objects.get_or_create(status="ok")


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.get(
    "/",
    tags=["Démarrage"],
    description="démarrage de l'API sur la page de documentation.",
)
def main():
    return RedirectResponse(url="/docs/")


@app.get(
    "/last_deployment_infos",
    tags=["Démarrage"],
    status_code=status.HTTP_200_OK,
    response_model=DeploymentInfo,
    description="Informations concernant le dernier déploiement du conteneur.",
)
def get_last_deployment_infos():
    info = DeploymentSettings()
    return DeploymentInfo(**info.dict())


@app.get(
    "/healthcheck/",
    tags=["healthcheck"],
    status_code=status.HTTP_200_OK,
    response_description="ok",
    summary="resume",
)
def get_api_status() -> str:
    return "ok"


@app.get(
    "/healthcheck_db_link/",
    tags=["healthcheck"],
    status_code=status.HTTP_200_OK,
    response_description="ok",
    summary="resume",
)
async def get_db_link_status() -> str:

    try:
        query = await Healthcheck.objects.get()
        query = query.status
    except ValueError:
        query = "ko"

    return query
