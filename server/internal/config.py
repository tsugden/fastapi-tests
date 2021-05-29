from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str
    JWT_SECRET: str
    HOST: str
    PORT: int
    DEBUG: bool

    class Config:
        env_file = ".env"
