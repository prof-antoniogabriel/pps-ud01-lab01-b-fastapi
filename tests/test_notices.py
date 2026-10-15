from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_list_notices() -> None:
    response = client.get("/api/notices/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_invalid_notice() -> None:
    response = client.post("/api/notices/", json={"title": "x", "severity": "critical"})
    assert response.status_code == 422
