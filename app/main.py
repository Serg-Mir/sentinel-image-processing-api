from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.core.config import settings
from app.core.logging import setup_logging

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

setup_logging()

app.include_router(api_router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
