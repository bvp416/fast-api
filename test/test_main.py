import app.main as main
from app.main import app
from unittest.mock import patch
from fastapi.testclient import TestClient

client = TestClient(app)

query = {
    "path": "/test1",
    "status": "safe"
}
@patch('app.main.return_query')
def test_get_resource_scan(mocked_query):
    mocked_query.return_value = query
    response = client.get('/urlinfo/1/google.com:443/?query=/test1')
    assert response.status_code == 200
    assert response.json() == query

def test_return_query_found():
    result = main.return_query('google.com:443', '/test1')
    assert result == main.db['google_com']['443'][0]

def test_return_query_not_found():
    result = main.return_query('google.com:443', '/foo')
    assert result == []
