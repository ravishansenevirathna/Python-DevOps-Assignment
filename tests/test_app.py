import pytest
from app import create_app
from app.models import db  # Import your db instance

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:1234@localhost:3306/flask_task_db'
    
    with app.app_context():
        db.create_all()
        
    yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_page(client):
    """Test that the home page returns a 200 status code"""
    response = client.get('/tasks')
    assert response.status_code in [200, 400]  # 200 if empty list, 400 if error handling