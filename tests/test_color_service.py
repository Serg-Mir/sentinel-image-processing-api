import pytest
import numpy as np
from app.services.color_service import get_main_color


def test_get_main_color():
    # Create a red image
    red_image = np.full((100, 100, 3), (255, 0, 0), dtype=np.uint8)
    assert get_main_color(red_image) == "Red"

    # Create a green image
    green_image = np.full((100, 100, 3), (0, 255, 0), dtype=np.uint8)
    assert get_main_color(green_image) == "Green"

    # Create a blue image
    blue_image = np.full((100, 100, 3), (0, 0, 255), dtype=np.uint8)
    assert get_main_color(blue_image) == "Blue"
