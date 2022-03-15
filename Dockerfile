# Dockerfile

FROM tiangolo/uvicorn-gunicorn:python3.8-slim

RUN apt-get update && apt-get install -y netcat

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY ./backend /app/

# # add entrypoint.sh
# COPY ./prestart.sh .
# RUN chmod +x /app/prestart.sh

# # run entrypoint.sh
# ENTRYPOINT ["/app/prestart.sh"]