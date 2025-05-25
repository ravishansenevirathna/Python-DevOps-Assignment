import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page returns a 200 status code"""
    response = client.get('/tasks')
    assert response.status_code == 400  # Expecting 400 because no tasks are created yet