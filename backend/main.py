from functools import lru_cache

from fastapi import Depends, FastAPI
import uvicorn

from internal.config import Settings


@lru_cache
def get_settings() -> Settings:
    return Settings()


#settings = Depends(get_settings())
settings = Settings()


def get_application() -> FastAPI:
    application = FastAPI()
    return application


app = get_application()


@app.get("/")
async def ping_pong():
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
