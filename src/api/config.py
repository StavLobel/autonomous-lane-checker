"""
Configuration management for the lane detection service.

This module provides Pydantic-based settings management with environment variable
support, validation, and type safety for the OpenCV Lane Detection API.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings with environment variable support and validation.
    
    All settings can be overridden via environment variables using uppercase names.
    For example: APP_NAME, DEBUG, HOST, PORT, etc.
    """
    model_config = SettingsConfigDict(
        env_file='config/settings.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'
    )
    
    # App metadata
    app_name: str = Field(
        default="Lane Detection API",
        description="Application name"
    )
    version: str = Field(
        default="0.1.0",
        description="API version"
    )
    
    # Environment and debugging
    environment: Literal["development", "testing", "production", "docker"] = Field(
        default="development",
        description="Runtime environment"
    )
    debug: bool = Field(
        default=True,
        description="Enable debug mode"
    )
    
    # Server configuration
    host: str = Field(
        default="0.0.0.0",
        description="Server host address"
    )
    port: int = Field(
        default=8000,
        ge=1,
        le=65535,
        description="Server port number"
    )
    
    # Image processing limits
    max_image_mb: float = Field(
        default=10.0,
        ge=0.1,
        le=100.0,
        description="Maximum image size in megabytes"
    )
    
    # OpenCV pipeline parameters
    canny_low: int = Field(
        default=50,
        ge=10,
        le=200,
        description="Canny edge detection low threshold"
    )
    canny_high: int = Field(
        default=150,
        ge=50,
        le=300,
        description="Canny edge detection high threshold"
    )
    gaussian_kernel: int = Field(
        default=5,
        ge=3,
        le=15,
        description="Gaussian blur kernel size (must be odd)"
    )
    hough_threshold: int = Field(
        default=15,
        ge=5,
        le=50,
        description="Hough transform threshold"
    )
    hough_min_line_length: int = Field(
        default=40,
        ge=10,
        le=200,
        description="Minimum line length for Hough transform"
    )
    hough_max_line_gap: int = Field(
        default=20,
        ge=5,
        le=100,
        description="Maximum line gap for Hough transform"
    )
    
    # ROI parameters (as ratios of image dimensions)
    roi_bottom_width: float = Field(
        default=0.9,
        ge=0.1,
        le=1.0,
        description="ROI bottom width ratio"
    )
    roi_top_width: float = Field(
        default=0.1,
        ge=0.05,
        le=0.5,
        description="ROI top width ratio"
    )
    roi_height: float = Field(
        default=0.6,
        ge=0.3,
        le=0.9,
        description="ROI height ratio"
    )
    
    # Performance thresholds
    perf_p95_ms: int = Field(
        default=200,
        ge=50,
        le=5000,
        description="P95 performance threshold in milliseconds"
    )
    
    # Model validation
    def model_post_init(self, __context) -> None:
        """Post-initialization validation."""
        # Ensure gaussian kernel is odd
        if self.gaussian_kernel % 2 == 0:
            self.gaussian_kernel += 1
        
        # Ensure canny high > canny low
        if self.canny_high <= self.canny_low:
            self.canny_high = self.canny_low * 2


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    
    Returns:
        Settings: Singleton settings instance with all configuration loaded
    """
    return Settings()
