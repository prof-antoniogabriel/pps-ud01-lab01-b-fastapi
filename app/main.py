from fastapi import FastAPI

from app.api.routes.notices import router as notices_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(notices_router, prefix="/api")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.app_env}
