"""Fixtures for the UI test suite (Playwright + SauceDemo)."""
import pytest

from config import UI_BASE_URL, UI_PASSWORD, UI_USERNAME


@pytest.fixture
def ui_base_url():
    return UI_BASE_URL


@pytest.fixture
def credentials():
    return {"username": UI_USERNAME, "password": UI_PASSWORD}
