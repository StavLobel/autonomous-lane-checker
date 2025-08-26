"""
Custom assertion utilities for lane detection tests.
"""

from typing import Any, Dict


def assert_lane_detection_response(response_data: Dict[str, Any]) -> None:
    """
    Assert that a lane detection response has the expected structure.
    
    TODO: Implement full validation in ALC-EP003-M05
    """
    # Basic structure validation
    assert "lanes" in response_data
    assert "processing_ms" in response_data
    assert "num_segments_used" in response_data
    assert "warnings" in response_data
    
    # Type validation
    assert isinstance(response_data["processing_ms"], (int, float))
    assert isinstance(response_data["num_segments_used"], int)
    assert isinstance(response_data["warnings"], list)


def assert_error_response(response_data: Dict[str, Any], expected_code: str = None) -> None:
    """
    Assert that an error response has the expected structure.
    
    TODO: Implement full validation in ALC-EP004-m01
    """
    assert "error" in response_data
    assert "code" in response_data["error"]
    assert "message" in response_data["error"]
    
    if expected_code:
        assert response_data["error"]["code"] == expected_code
