import unittest
from unittest.mock import patch
import numpy as np
from app.services.sentinel_service import get_sentinel_image


class TestGetSentinelImage(unittest.TestCase):
    @patch("app.services.sentinel_service.SentinelHubRequest")
    def test_get_sentinel_image(self, mock_sentinel_hub_request):
        mock_request_instance = mock_sentinel_hub_request.return_value
        dummy_image_array = np.zeros((512, 512, 3), dtype=np.uint8)
        mock_request_instance.get_data.return_value = [dummy_image_array]

        bbox = [
            13.822174072265625,
            45.85080395917834,
            14.55963134765625,
            46.29191774991382,
        ]

        image = get_sentinel_image(bbox)

        self.assertIsInstance(image, np.ndarray)
        self.assertEqual(image.shape, (512, 512, 3))
        np.testing.assert_array_equal(image, dummy_image_array)

        mock_sentinel_hub_request.assert_called_once()

        mock_sentinel_hub_request.assert_called_with(
            evalscript=unittest.mock.ANY,
            input_data=unittest.mock.ANY,
            responses=unittest.mock.ANY,
            bbox=unittest.mock.ANY,
            size=(512, 512),
            config=unittest.mock.ANY,
        )
