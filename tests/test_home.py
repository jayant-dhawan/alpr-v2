from fastapi.testclient import TestClient
from pathlib import Path

from app.main import app

client = TestClient(app)


def test_home_page_route_exist():
    response = client.get("/")
    assert response.status_code == 200

def test_number_plate_route_exist():
    response = client.post(
        '/read-plate',
        files={"file": ("car.jpeg", open(str(Path().absolute()) + '/tests/test_images/car.jpeg', "rb"), "image/jpeg")}
    )
    assert response.status_code == 200

def test_read_number_plate_from_image():
    response = client.post(
        '/read-plate',
        files={"file": ("car.jpeg", open(str(Path().absolute()) + '/tests/test_images/car.jpeg', "rb"), "image/jpeg")}
    )
    assert response.json() == 'DL8CAF5030'
