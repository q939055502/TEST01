from fastapi import FastAPI

from src.config.settings import settings
from src.api.routes import router

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(router, prefix=settings.api_prefix)


@app.get("/")
def read_root():
    return {"msg": "Welcome to the Test API", "app_name": settings.app_name}