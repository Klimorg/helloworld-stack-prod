from pathlib import Path
from typing import Optional

import arrow
import requests
import streamlit as st
from dependancies import check_password
from pydantic import BaseModel


class RequestResponse(BaseModel):
    status_code: int
    headers: dict[str, str]
    encoding: Optional[str]
    text: str


if check_password():
    st.title("Hello World stack prod")

    test = st.button(label="healthcheck")

    if test:
        result = requests.get(url="http://backend:8000/healthcheck")

        result = RequestResponse(
            status_code=result.status_code,
            headers=result.headers,
            encoding=result.encoding,
            text=result.text,
        )
        st.text(f"{result}")

    st.text("Renseigner une nouvelle inférence.")

    num_detections = st.number_input(label="Nombre d'objets détectés", value=0)
    confidence = st.number_input(label="score", value=1.0)

    record = st.button(label="Enregister")

    if record:
        result = requests.post(
            url="http://backend:8000/inferences/",
            json={
                "inference_date": arrow.now().format("YYYY-MM-DD"),
                "inference_time": arrow.now().format("HH:mm:ss"),
                "num_detections": num_detections,
                "confidence": confidence,
            },
        )
        result.text
