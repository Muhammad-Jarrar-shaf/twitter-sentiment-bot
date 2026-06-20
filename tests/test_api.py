from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_summary():
    response = client.get("/summary")

    assert response.status_code == 200

def test_health():
     response = client.get("/health")

     assert response.status_code == 200
     assert response.json()["status"] == "healthy"