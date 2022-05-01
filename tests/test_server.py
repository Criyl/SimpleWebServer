from server import __version__, app
from fastapi.testclient import TestClient


def test_version() -> None:
    assert __version__ == '1.0.0'


def test_request() -> None:
    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"msg": "hello world"}
