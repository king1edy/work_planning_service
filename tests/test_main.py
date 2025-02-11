import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_worker():
    response = client.post("/workers/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
