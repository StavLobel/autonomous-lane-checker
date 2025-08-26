"""
FastAPI main application entry point for lane detection service.

This module provides the main FastAPI app instance with health and version endpoints,
proper lifespan management, and application startup/shutdown handling.
"""

import logging
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    
    Handles startup and shutdown logic:
    - Startup: Initialize resources, load models, setup connections
    - Shutdown: Cleanup resources, close connections
    """
    # Startup
    logger.info("Starting up Lane Detection API...")
    logger.info(f"Environment: {settings.environment}")
    logger.info(f"Max image size: {settings.max_image_mb}MB")
    app.state.startup_complete = True
    
    yield
    
    # Shutdown
    logger.info("Shutting down Lane Detection API...")
    app.state.startup_complete = False


app = FastAPI(
    title="Lane Detection API",
    description="OpenCV-based lane detection service for automotive QA automation demo",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
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
async def health_check() -> Dict[str, Any]:
    """
    Health check endpoint for liveness and readiness probes.
    
    Returns:
        Dict containing health status and system information
    """
    return {
        "status": "healthy",
        "service": "lane-detection-api",
        "version": "0.1.0",
        "startup_complete": getattr(app.state, 'startup_complete', False),
        "environment": settings.environment
    }


@app.get("/version")
async def get_version() -> Dict[str, Any]:
    """
    Get API version and configuration information.
    
    Returns:
        Dict containing version and configuration details
    """
    return {
        "service": "lane-detection-api",
        "api_version": "0.1.0",
        "opencv_enabled": True,
        "max_image_mb": settings.max_image_mb,
        "environment": settings.environment,
        "docs_url": "/docs"
    }


@app.get("/")
async def root() -> Dict[str, str]:
    """
    Root endpoint with basic API information and navigation.
    
    Returns:
        Dict containing welcome message and documentation links
    """
    return {
        "message": "OpenCV Lane Detection API",
        "description": "Automotive QA automation demo service",
        "docs": "/docs",
        "health": "/health",
        "version": "/version"
    }


# TODO: Add POST /lanes endpoint - will be implemented in ALC-EP002-M08
