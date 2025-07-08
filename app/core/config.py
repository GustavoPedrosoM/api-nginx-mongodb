from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "API Base"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
