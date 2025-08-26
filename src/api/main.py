"""
FastAPI main application entry point for lane detection service.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings

settings = get_settings()

app = FastAPI(
    title="Lane Detection API",
    description="OpenCV-based lane detection service for automotive QA automation demo",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint for liveness probes."""
    return {"status": "ok"}


@app.get("/version")
async def get_version():
    """Get API version and configuration info."""
    return {
        "api_version": "0.1.0",
        "opencv_enabled": True,
        "max_image_mb": settings.max_image_mb,
        "environment": settings.environment
    }


# TODO: Add POST /lanes endpoint - will be implemented in ALC-EP002-M08
