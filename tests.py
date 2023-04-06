import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.mark.parametrize(
    argnames=["days", "expected"],
    argvalues=[
        (1, [175]),
        (3, [175, 185, 175]),
        (7, [171, 212, 212, 144, 175, 185, 175]),
    ],
)
def test_predict(client, days, expected):
    response = client.get(f"/predict?days={days}")
    response_data = response.json()
    assert expected == response_data["result"]
    assert response.status_code == 200
