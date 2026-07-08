"""Упражнение 2 — перехват и мок сети через page.route.

Демонстрация: перехватываем и блокируем загрузку изображений на SauceDemo
и считаем количество перехваченных запросов. Тот же механизм через
route().fulfill() позволяет подменять ответы API на моковые данные.

Запуск:  pytest playwright_practice/exercise_02_network_mock.py -s

TODO (день 5): сделай route(), который fulfill() отдаёт моковый JSON для
API-приложения, и проверь, что интерфейс отобразил именно мок (а не реальные данные).
"""
import re

import pytest

from config import UI_BASE_URL, UI_PASSWORD, UI_USERNAME

pytestmark = pytest.mark.ui


def test_block_images_via_route(page):
    intercepted = {"count": 0}

    def handle(route):
        intercepted["count"] += 1
        route.abort()

    # перехватываем все картинки ещё до навигации
    page.route(re.compile(r"\.(png|jpe?g|svg)(\?|$)"), handle)

    page.goto(UI_BASE_URL)
    page.get_by_placeholder("Username").fill(UI_USERNAME)
    page.get_by_placeholder("Password").fill(UI_PASSWORD)
    page.get_by_role("button", name="Login").click()

    # на странице товаров есть изображения — значит перехват сработал
    assert intercepted["count"] > 0
