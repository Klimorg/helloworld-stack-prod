from fastapi.testclient import TestClient

# import stack_prod.backend
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/healthcheck/")
    assert response.status_code == 200


def test_read_main2():
    response = client.get("/healthcheck/")
    assert response.status_code == 201
