"""
Pydantic schemas for request/response models.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class LaneDetectionRequest(BaseModel):
    """Request model for lane detection."""
    # TODO: Implement in ALC-EP002-M07
    pass


class Lane(BaseModel):
    """Model for a detected lane line."""
    x1: int = Field(..., description="Start point x coordinate")
    y1: int = Field(..., description="Start point y coordinate") 
    x2: int = Field(..., description="End point x coordinate")
    y2: int = Field(..., description="End point y coordinate")
    slope: float = Field(..., description="Lane line slope")


class LaneDetectionResponse(BaseModel):
    """Response model for lane detection results."""
    lanes: dict = Field(..., description="Detected left and right lanes")
    lane_width_px: Optional[int] = Field(None, description="Lane width in pixels")
    center_offset_px: Optional[float] = Field(None, description="Center offset in pixels")
    num_segments_used: int = Field(..., description="Number of line segments used")
    processing_ms: float = Field(..., description="Processing time in milliseconds")
    warnings: List[str] = Field(default_factory=list, description="Processing warnings")
    overlay_png_b64: Optional[str] = Field(None, description="Base64 encoded overlay image")


class ErrorResponse(BaseModel):
    """Standard error response model."""
    error: dict = Field(..., description="Error details")
    
    class Config:
        schema_extra = {
            "example": {
                "error": {
                    "code": "INVALID_INPUT",
                    "message": "Image format not supported"
                }
            }
        }
