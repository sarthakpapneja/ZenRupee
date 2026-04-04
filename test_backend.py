import pytest
from server import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_dashboard_requires_auth(client):
    res = client.get("/api/dashboard/summary")
    assert res.status_code == 401

def test_login_wrong_password(client):
    res = client.post("/api/login", json={"username": "john_doe", "password": "wrong"})
    assert res.status_code == 401

def test_customer_cannot_delete_transaction(client):
    client.post("/api/login", json={"username": "john_doe", "password": "password123"})
    res = client.delete("/api/transactions/1")
    assert res.status_code == 403

def test_manager_can_access_users(client):
    client.post("/api/login", json={"username": "mgr_admin", "password": "admin123"})
    res = client.get("/api/users")
    assert res.status_code == 200
