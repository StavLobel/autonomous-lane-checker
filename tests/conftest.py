"""
PyTest configuration and shared fixtures.
"""

import asyncio
from typing import AsyncGenerator

import pytest
from playwright.async_api import APIRequestContext, Playwright, async_playwright

from src.api.config import get_settings

settings = get_settings()


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def playwright_instance() -> AsyncGenerator[Playwright, None]:
    """Playwright instance for the test session."""
    async with async_playwright() as p:
        yield p


@pytest.fixture(scope="session")
async def api_client(playwright_instance: Playwright) -> AsyncGenerator[APIRequestContext, None]:
    """
    API client for testing the lane detection service.
    
    TODO: Implement full fixture in ALC-EP003-M01
    """
    # Create API request context
    request_context = await playwright_instance.request.new_context(
        base_url=f"http://localhost:{settings.port}",
        extra_http_headers={
            "Content-Type": "application/json"
        }
    )
    
    yield request_context
    
    await request_context.dispose()


@pytest.fixture
def sample_image_path():
    """Path to sample test image."""
    # TODO: Implement in ALC-EP001-m03
    return "data/images/highway_sample.jpg"


@pytest.fixture
def no_markings_image_path():
    """Path to image with no lane markings."""
    # TODO: Implement in ALC-EP001-m03
    return "data/images/no_markings.jpg"


# Pytest markers
pytest.mark.functional = pytest.mark.functional
pytest.mark.negative = pytest.mark.negative
pytest.mark.edge = pytest.mark.edge
pytest.mark.performance = pytest.mark.performance
