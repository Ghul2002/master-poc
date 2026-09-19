import pytest
from fastapi.testclient import TestClient
from main import app, calculate_discount

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_calculate_discount_valid():
    assert calculate_discount(100.0, 20.0) == 80.0
    assert calculate_discount(50.0, 0.0) == 50.0

def test_calculate_discount_invalid():
    with pytest.raises(ValueError):
        calculate_discount(-10.0, 10.0)
    with pytest.raises(ValueError):
        calculate_discount(100.0, 150.0)

def test_discount_endpoint():
    response = client.get("/discount?price=200&discount=15")
    assert response.status_code == 200
    assert response.json()["final_price"] == 170.0