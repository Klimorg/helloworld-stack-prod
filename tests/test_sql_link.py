# from app.db import database
# from fastapi.testclient import TestClient
# from app.main import app

# app.state.database = database


# client = TestClient(app)


# def test_create_user():
#     response = client.post(
#         "/inferences/",
#         {
#             "inference_date": "2022-03-25",
#             "inference_time": "14:35:50",
#             "num_detections": 0,
#             "confidence": 1,
#         },
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["num_detections"] == 0
#     assert "id" in data
# id = data["id"]

# response = client.get(f"/users/{user_id}")
# assert response.status_code == 200, response.text
# data = response.json()
# assert data["email"] == "deadpool@example.com"
# assert data["id"] == user_id
