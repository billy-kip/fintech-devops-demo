import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "running"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_transaction():
    client = app.test_client()

    response = client.get("/transaction")

    assert response.status_code == 200
    assert response.json["status"] == "successful"


def test_api_info():
    client = app.test_client()

    response = client.get("/api-info")

    assert response.status_code == 200
    assert response.json["service"] == "Fintech Demo API"
    assert response.json["version"] == "1.0"
    assert response.json["environment"] == "development"