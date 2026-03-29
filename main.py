from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Request, status, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from src.backend_template.api.v1.api import router as api_router
from src.backend_template.core.config import Settings
from src.backend_template.core.logger import logger
from src.backend_template.core.security import verify_token
from src.backend_template.db.session import get_session
from src.backend_template.redis.client import redis_client
from sqlalchemy.ext.asyncio import AsyncSession

limiter = Limiter(key_func=get_remote_address, default_limits=["200 per minute"])

settings = Settings()

@asynccontextmanager
async def lifespan(app_: FastAPI):
    # Startup: Connect DB, Redis
    logger.info("Starting up...")
    await redis_client.connect()
    logger.info("Redis connected")
    yield
    # Shutdown
    await redis_client.disconnect()
    logger.info("Shutdown complete")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


async def _rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    logger.warning("Rate limit exceeded", ip=get_remote_address(request), path=request.url.path)
    raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded")


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/ready", tags=["health"])
async def readiness_check(session: Annotated[AsyncSession, Depends(get_session)]):
    """Readiness probe: checks DB connection."""
    try:
        await session.execute("SELECT 1")
        return {"status": "ready"}
    except Exception as e:
        logger.error("DB readiness failed", error=str(e))
        raise HTTPException(status_code=503, detail="DB not ready")


@app.get("/metrics")
async def metrics():
    """Prometheus metrics placeholder."""
    return {"metrics": "TODO: prometheus_client"}

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend_template.main:app", host="0.0.0.0", port=8000, reload=True)
Tani jepmë të gjithë projektin si një listë të plotë të skedarëve me path-in e tyre.

Për çdo skedar shkruaj në këtë format:

```filepath: backend_template/pyproject.toml
[përmbajtja e plotë e kodit këtu]
