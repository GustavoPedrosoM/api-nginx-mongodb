from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "API FastAPI Studies"
    mongo_uri: str  # <-- Adicione essa linha

    class Config:
        env_file = ".env"

settings = Settings()