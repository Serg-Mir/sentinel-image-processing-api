from io import BytesIO
from PIL import Image
import numpy as np


def numpy_to_image(image: np.ndarray) -> BytesIO:
    """Convert numpy array to image bytes."""
    img = Image.fromarray(image.astype("uint8"))
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)
    return img_byte_arr
