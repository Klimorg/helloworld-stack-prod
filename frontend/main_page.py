from typing import Optional
import streamlit as st
import requests
from pydantic import BaseModel
from dependancies import check_password
from pathlib import Path


class RequestResponse(BaseModel):
    status_code: int
    headers: dict[str, str]
    encoding: Optional[str]
    text: str


def post_request(root: Path, endpoint: str, *args, **kwargs):
    pass


def get_request(root: str, endpoint: str) -> requests.Response:

    return requests.get(url=f"{root}/{endpoint}")


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
