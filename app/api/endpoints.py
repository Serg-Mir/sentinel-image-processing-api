from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from fastapi.responses import StreamingResponse
from app.services.sentinel_service import get_sentinel_image
from app.services.color_service import get_main_color
from app.utils.image_utils import numpy_to_image
from io import BytesIO
import numpy as np
from PIL import Image

router = APIRouter()


@router.get("/image")
async def get_image(
    bbox=Query(
        "13.822174072265625,45.85080395917834,14.55963134765625,46.29191774991382",
        description="Bounding box coordinates (min_lon,min_lat,max_lon,max_lat)",
    )
):
    """Show the Sentinel image as a FastAPI response."""
    try:
        bbox = list(map(float, bbox.split(",")))
        image = get_sentinel_image(bbox)
        img_byte_arr = numpy_to_image(image)
        return StreamingResponse(img_byte_arr, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/image-with-color")
async def get_image_with_color(
    bbox=Query(
        "-0.52,38.32,-0.44, 38.37",
        description="Bounding box coordinates (min_lon,min_lat,max_lon,max_lat)",
    )
):
    """Show the Sentinel image and print the main color name."""
    try:
        bbox = list(map(float, bbox.split(",")))
        image = get_sentinel_image(bbox)
        color_name = get_main_color(image)
        img_byte_arr = numpy_to_image(image)

        headers = {"X-Main-Color": color_name}
        return StreamingResponse(img_byte_arr, media_type="image/png", headers=headers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    """Upload an image and get its main color."""
    try:
        contents = await file.read()
        img = Image.open(BytesIO(contents))
        img_array = np.array(img)
        color_name = get_main_color(img_array)
        return {"main_color": color_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
