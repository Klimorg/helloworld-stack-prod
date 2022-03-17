# Dockerfile

FROM tiangolo/uvicorn-gunicorn:python3.8-slim

RUN apt-get update && apt-get install --no-install-recommends -y netcat && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./backend /app/
