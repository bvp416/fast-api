from fastapi.testclient import TestClient
import app.main as main
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@patch('app.main.return_query')
def test_get_resource_scan(mocked_query):
    query = {
        'name' : 'youtube.com',
        'status' : 'safe'
    }
    mocked_query.return_value = query
    response = client.get('/urlinfo/1/foo/youtube.com')
    assert response.status_code == 200
    assert response.json() == query

def test_return_query():
    result = main.return_query('youtube.com')
    assert result == main.db[0]
