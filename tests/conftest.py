import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

@pytest.fixture
def competitions():
    competitions = [
        {"club": "Simply Lift",
        "competition": "Spring Festival",
        "places": "10"},

    ]
    return competitions

@pytest.fixture
def users():
    users = [
        {'email': ['john@simplylift.co', 'wrongemail@simplylift.co']}
    ]
    return users