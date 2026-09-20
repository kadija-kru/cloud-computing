from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_duplicate_event_is_not_reprocessed():
    payload = {
        "source": "edge-router-01",
        "event_type": "auth_failure",
        "severity": 8,
        "message": "Repeated authentication failures detected"
    }

    first = client.post("/events", json=payload)
    second = client.post("/events", json=payload)

    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["fingerprint"] == second.json()["fingerprint"]
    assert second.json()["duplicate"] is True
    assert second.json()["risk"] == "critical"

def test_validation_rejects_invalid_severity():
    response = client.post("/events", json={
        "source": "router",
        "event_type": "link_down",
        "severity": 50,
        "message": "invalid"
    })
    assert response.status_code == 422
