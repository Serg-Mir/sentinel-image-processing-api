import numpy as np
from PIL import Image
import logging

logger = logging.getLogger(__name__)


def get_main_color(image: np.ndarray) -> str:
    """Get the main color name of the image."""
    try:
        img = Image.fromarray(image.astype("uint8"), "RGB")
        colors = img.getcolors(img.size[0] * img.size[1])
        max_color = max(colors, key=lambda x: x[0])[1]

        color_ranges = {
            "Red": ((200, 0, 0), (255, 60, 60)),
            "Green": ((0, 200, 0), (60, 255, 60)),
            "Blue": ((0, 0, 200), (60, 60, 255)),
            "Yellow": ((200, 200, 0), (255, 255, 60)),
            "Cyan": ((0, 200, 200), (60, 255, 255)),
            "Magenta": ((200, 0, 200), (255, 60, 255)),
            "White": ((200, 200, 200), (255, 255, 255)),
            "Black": ((0, 0, 0), (60, 60, 60)),
        }

        for color_name, (lower, upper) in color_ranges.items():
            if all(lower[i] <= max_color[i] <= upper[i] for i in range(3)):
                return color_name

        return "Unknown"
    except Exception as e:
        logger.error(f"Error in get_main_color: {str(e)}")
        raise
