import pytest
from fastapi.testclient import TestClient


def test_health_check(test_client: TestClient):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# ToDo: consider adding related mocks
# def test_get_image(test_client: TestClient):
#     response = test_client.get("/api/image")
#     assert response.status_code == 200
#     assert response.headers["content-type"] == "image/png"
#
#
# def test_get_image_with_color(test_client: TestClient):
#     response = test_client.get("/api/image-with-color")
#     assert response.status_code == 200
#     assert response.headers["content-type"] == "image/png"
#     assert "X-Main-Color" in response.headers


def test_upload_image(test_client: TestClient):
    # Create a dummy image for testing
    from PIL import Image
    import io

    img = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    response = test_client.post(
        "/api/upload-image", files={"file": ("test.png", img_byte_arr, "image/png")}
    )
    assert response.status_code == 200
    assert "main_color" in response.json()
