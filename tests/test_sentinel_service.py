import pytest
from app.services.sentinel_service import get_sentinel_image
import numpy as np


def test_get_sentinel_image():
    bbox = [13.822174072265625, 45.85080395917834, 14.55963134765625, 46.29191774991382]
    image = get_sentinel_image(bbox)
    assert isinstance(image, np.ndarray)
    assert image.shape == (512, 512, 3)
