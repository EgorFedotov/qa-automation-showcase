# 🎓 Playwright — практика (день 1–7)

Учебная песочница. Файлы здесь **не входят** в основной прогон (`pytest` собирает только `tests/`)
и не ломают CI. Запускаешь вручную, разбираешься, потом переносишь приёмы в `tests/ui`.

Главный источник — официальная дока: https://playwright.dev/python/docs/intro

## Как запускать упражнения
```bash
pytest playwright_practice/exercise_01_locators.py --headed     # видимый браузер
pytest playwright_practice/exercise_02_network_mock.py -s        # с выводом
```

## План на неделю (отмечай по мере прохождения)
- [ ] **День 1 — Локаторы + auto-waiting.** Дока: *Locators*, *Auto-waiting*. Разбери `exercise_01`,
      потом перепиши `tests/ui/pages/*.py` на `get_by_role`/`get_by_placeholder`/`get_by_test_id`.
- [ ] **День 2 — Web-first assertions.** Дока: *Assertions*. Замени ручные `assert` на
      `expect(locator).to_be_visible()` и т.п. с авто-ретраем.
- [ ] **День 3 — Codegen.** `playwright codegen https://www.saucedemo.com` — запиши сценарий
      чекаута, причеши в Page Object, добавь тест в `tests/ui`.
- [ ] **День 4 — Trace Viewer.** См. `exercise_03_trace_and_debug.md`. Прогони с трейсингом,
      открой трейс, разбери шаги.
- [ ] **День 5 — Network (`page.route`).** Разбери `exercise_02`, затем сделай `route().fulfill()`
      с моковым JSON и проверь, что UI отобразил мок.
- [ ] **День 6 — Auth через `storage_state`.** Дока: *Authentication*. Залогинься один раз,
      сохрани состояние, переиспользуй в тестах (быстрее прогон).
- [ ] **День 7 — Кроссбраузерность.** Прогони UI на трёх движках:
      `pytest tests/ui --browser chromium --browser firefox --browser webkit`.
- [ ] **Неделя 2 — база TypeScript.** Переложи 2–3 теста на TS-Playwright (тот же API, другой
      синтаксис), чтобы не отсекаться от TS-вакансий.

## Инструменты-must
- `playwright codegen <url>` — запись теста кликами
- `pytest --tracing on` + `playwright show-trace trace.zip` — пошаговый разбор падения
- `pytest --headed --slowmo 500` — смотреть глазами
