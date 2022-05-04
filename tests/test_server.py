from server import app
from fastapi.testclient import TestClient


def test_request() -> None:
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["msg"] == "hello world"
