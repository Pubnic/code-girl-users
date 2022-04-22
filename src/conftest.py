import pytest
from fastapi.testclient import TestClient


# @pytest.fixture(scope='function')
# def django_db_setup(django_db_setup, django_db_blocker, settings):
#     with django_db_blocker.unblock():
#         from scripts import PopulateDB, CleanDB
#         CleanDB()
#         PopulateDB()


@pytest.fixture(scope='function')
def client():
    from app import app
    client = TestClient(app)
    return client


