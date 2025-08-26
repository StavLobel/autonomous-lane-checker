"""
Configuration management for the lane detection service.
"""

import os
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    # Environment
    environment: str = "development"
    debug: bool = True
    
    # API Settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Image processing limits
    max_image_mb: float = 10.0
    
    # OpenCV pipeline parameters
    canny_low: int = 50
    canny_high: int = 150
    gaussian_kernel: int = 5
    hough_threshold: int = 15
    hough_min_line_length: int = 40
    hough_max_line_gap: int = 20
    
    # ROI parameters (as ratios of image dimensions)
    roi_bottom_width: float = 0.9
    roi_top_width: float = 0.1
    roi_height: float = 0.6
    
    # Performance thresholds
    perf_p95_ms: int = 200
    
    class Config:
        env_file = "config/settings.env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
