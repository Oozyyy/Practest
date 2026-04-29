import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_json(client):
    response = client.get('/')
    assert response.is_json
    assert response.get_json() == {"message": "Hello, DevOps!"}
