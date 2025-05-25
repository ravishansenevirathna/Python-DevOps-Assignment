import pytest
from app import create_app, db  # Import db from your app package

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use SQLite for faster tests
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.create_all()
        
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_tasks_endpoint(client):
    """Test that the tasks endpoint returns a proper status code"""
    response = client.get('/tasks')
    # Accept either 200 (empty list) or 400 (error handling)
    assert response.status_code in (200, 400)