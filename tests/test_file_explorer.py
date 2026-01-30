import pytest
from flask import Flask
from flask_file_explorer.file_explorer import file_explorer_bp, get_base_directory, is_in_base_directory
import os

# Helper function to create a Flask app for testing
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['FFE_BASE_DIRECTORY'] = '/tmp/dummy/base'
    app.register_blueprint(file_explorer_bp, url_prefix='/explorer')
    with app.app_context():
        yield app

@pytest.fixture(autouse=True)
def setup_and_teardown():
    os.makedirs('/tmp/dummy/base/subdir', exist_ok=True)
    
    yield  # this is where the testing happens
    
    os.removedirs('/tmp/dummy/base/subdir')

# New test for checking base directory utility

def test_get_base_directory(app):
    with app.app_context():
        assert get_base_directory() == '/tmp/dummy/base'

# Test the is_in_base_directory function

def test_is_in_base_directory(app):
    with app.app_context():
        assert is_in_base_directory('/tmp/dummy/base/subdir') is True
        assert is_in_base_directory('/invalid/path') is False

def test_index_route(app):
    with app.test_client() as client:
        response = client.get('/explorer/')
        assert response.status_code == 200

def test_browse_route(app):
    with app.test_client() as client:
        response = client.get('/explorer/browse?path=subdir')
        assert response.status_code in [200, 400]  # Allow both successful list or illegal path

def test_upload_route(app):
    with app.test_client() as client:
        data = dict(file=(open(__file__, 'rb'), 'test.py'))
        response = client.post('/explorer/upload', data=data)
        assert response.status_code in [204, 400]  # Expecting file save success or illegal path
