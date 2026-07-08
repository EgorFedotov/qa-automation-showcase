"""Упражнение 1 — идиоматичные локаторы Playwright + web-first assertions.

В основном POM (tests/ui/pages) используются CSS-селекторы (#user-name, #password).
Playwright рекомендует user-facing локаторы: get_by_role / get_by_placeholder /
get_by_text — они устойчивее к изменениям вёрстки и читаются как действия пользователя.

Запуск:  pytest playwright_practice/exercise_01_locators.py --headed

TODO (день 1): перенеси этот стиль локаторов в tests/ui/pages/*.py.
"""
import re

import pytest
from playwright.sync_api import expect

from config import UI_BASE_URL, UI_PASSWORD, UI_USERNAME

pytestmark = pytest.mark.ui


def test_login_with_semantic_locators(page):
    page.goto(UI_BASE_URL)

    # user-facing локаторы вместо #user-name / #password
    page.get_by_placeholder("Username").fill(UI_USERNAME)
    page.get_by_placeholder("Password").fill(UI_PASSWORD)
    page.get_by_role("button", name="Login").click()

    # web-first assertions с авто-ретраем — не нужен ручной wait
    expect(page).to_have_url(re.compile(r"inventory\.html"))
    expect(page.get_by_text("Products")).to_be_visible()
