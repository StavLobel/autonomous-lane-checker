"""
Drawing utilities for lane detection overlays.
"""

import base64
from io import BytesIO
from typing import Dict, Optional

import cv2
import numpy as np
from PIL import Image


def draw_lane_overlay(image: np.ndarray, lanes: Dict, roi_mask: Optional[np.ndarray] = None) -> np.ndarray:
    """
    Draw lane detection overlay on image.
    
    Args:
        image: Original image
        lanes: Detected lanes dictionary
        roi_mask: Optional ROI mask to overlay
        
    Returns:
        Image with lane overlay drawn
    """
    # TODO: Implement in ALC-EP002-M06
    overlay = image.copy()
    
    # Mock overlay - draw simple lines
    if "left" in lanes and lanes["left"]:
        left = lanes["left"]
        cv2.line(overlay, (left["x1"], left["y1"]), (left["x2"], left["y2"]), (255, 0, 0), 3)
    
    if "right" in lanes and lanes["right"]:
        right = lanes["right"]
        cv2.line(overlay, (right["x1"], right["y1"]), (right["x2"], right["y2"]), (0, 0, 255), 3)
    
    return overlay


def image_to_base64(image: np.ndarray) -> str:
    """Convert OpenCV image to base64 PNG string."""
    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convert to PIL Image
    pil_image = Image.fromarray(rgb_image)
    
    # Save to base64
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    buffer.seek(0)
    
    return base64.b64encode(buffer.getvalue()).decode("utf-8")
