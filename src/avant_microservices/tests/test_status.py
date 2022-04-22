import pytest
from fastapi.testclient import TestClient


class TestStatus:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.url = '/avant-microservices/status'

    def test_status_ok(self, client: TestClient):
        response = client.get(self.url)
        assert response.status_code == 200
        assert response.json() == {'status': 'OK'}
