from sentinelhub import SHConfig, BBox, CRS, SentinelHubRequest, DataCollection
from sentinelhub import MimeType
from datetime import datetime, timedelta
import numpy as np
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

config = SHConfig()
config.sh_client_id = settings.SH_CLIENT_ID
config.sh_client_secret = settings.SH_CLIENT_SECRET


def get_sentinel_image(bbox: list) -> np.ndarray:
    """Retrieve Sentinel-2 image for the given bounding box."""
    try:
        bbox_obj = BBox(bbox=bbox, crs=CRS.WGS84)
        time_interval = (datetime.now() - timedelta(days=30), datetime.now())

        request = SentinelHubRequest(
            evalscript="""
                //VERSION=3
                function setup() {
                    return {
                        input: [{
                            bands: ["B02", "B03", "B04"]
                        }],
                        output: {
                            bands: 3
                        }
                    };
                }

                function evaluatePixel(sample) {
                    return [sample.B04, sample.B03, sample.B02];
                }
            """,
            input_data=[
                SentinelHubRequest.input_data(
                    data_collection=DataCollection.SENTINEL2_L2A,
                    time_interval=time_interval,
                )
            ],
            responses=[SentinelHubRequest.output_response("default", MimeType.PNG)],
            bbox=bbox_obj,
            size=(512, 512),
            config=config,
        )

        return request.get_data()[0]
    except Exception as e:
        logger.error(f"Error in get_sentinel_image: {str(e)}")
        raise
