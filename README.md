# QA Automation Showcase — Python · Playwright · REST API · Load · CI/CD

[![CI](https://github.com/EgorFedotov/qa-automation-showcase/actions/workflows/ci.yml/badge.svg)](https://github.com/EgorFedotov/qa-automation-showcase/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.49-green)
![pytest](https://img.shields.io/badge/pytest-8.3-orange)

Демонстрационный фреймворк автоматизации тестирования: **API + UI + нагрузка**, с отчётами
Allure и рабочими пайплайнами **GitHub Actions** и **GitLab CI**. Один репозиторий закрывает
весь цикл backend/UI QA — от юнита формы до нагрузочного профиля.

## 🧰 Стек

| Слой | Инструменты |
|---|---|
| Язык | Python 3.12 |
| API-тесты | `requests` + `pytest` (auth, CRUD, негативные проверки) |
| UI-тесты | `Playwright` + `pytest-playwright`, **Page Object Model** |
| Нагрузка | `Locust` |
| Отчётность | `Allure` (+ скриншот в отчёт при падении UI-теста) |
| CI/CD | GitHub Actions · GitLab CI |
| Качество кода | `flake8` |

**Объекты тестирования** — публичные учебные стенды: [restful-booker](https://restful-booker.herokuapp.com)
(API, auth + CRUD) и [SauceDemo](https://www.saucedemo.com) (UI, логин/корзина/чекаут).

## 📁 Структура

```
qa-automation-showcase/
├── config.py                 # конфиг из ENV (.env)
├── conftest.py               # Allure-скриншот при падении UI-теста
├── pytest.ini                # маркеры api/ui, alluredir
├── requirements.txt
├── tests/
│   ├── api/
│   │   ├── conftest.py        # session, auth_token, new_booking (+ health-skip)
│   │   └── test_booking_api.py
│   └── ui/
│       ├── conftest.py
│       ├── pages/             # Page Object Model
│       │   ├── login_page.py
│       │   ├── inventory_page.py
│       │   └── cart_page.py
│       └── test_saucedemo_ui.py
├── load/
│   └── locustfile.py          # нагрузочный профиль
├── .github/workflows/ci.yml   # GitHub Actions (lint → api → ui)
└── .gitlab-ci.yml             # GitLab CI (тот же пайплайн)
```

## 🚀 Запуск

```bash
# 1. окружение
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium

# 2. все тесты
pytest

# только API / только UI
pytest -m api
pytest -m ui

# UI в видимом браузере
pytest -m ui --headed
```

### Отчёт Allure
```bash
pytest                       # результаты пишутся в allure-results/
allure serve allure-results  # открыть интерактивный отчёт
```

### Нагрузочный тест
```bash
locust -f load/locustfile.py --host https://restful-booker.herokuapp.com \
    --users 20 --spawn-rate 5 --run-time 1m --headless
```

## ✅ Что покрыто

- **API:** авторизация и получение токена, полный CRUD брони, негативная проверка
  (после удаления — 404), автоочистка данных в teardown, health-check стенда со
  «скипом» при недоступности (CI не краснеет от чужого сервера).
- **UI:** успешный логин, ошибка для заблокированного пользователя, добавление товара
  в корзину и проверка бейджа/содержимого — через Page Object Model.
- **CI/CD:** линт → API-тесты → UI-тесты (с установкой браузеров), Allure-результаты
  выгружаются артефактами. Пайплайн продублирован под GitLab CI.

## 👤 Автор

**Егор Фёдотов** — QA Automation Engineer (Python / Java)
Telegram: [@egorkaafedotov](https://t.me/egorkaafedotov) · egorfedotovarz@gmail.com
