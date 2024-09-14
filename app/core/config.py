from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Sentinel Image Processing API"
    PROJECT_VERSION: str = "1.0.0"
    SH_CLIENT_ID: str
    SH_CLIENT_SECRET: str

    class Config:
        env_file = ".env"


settings = Settings()
