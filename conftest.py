"""Глобальные фикстуры фреймворка."""

import sys
from collections.abc import Callable, Generator
from pathlib import Path
from typing import Any

import allure
import pytest
from _pytest.fixtures import SubRequest

from core.browser_data import BrowserData


@pytest.fixture(scope='session', autouse=True)
def add_allure_env_property(
    request: SubRequest,
) -> Generator[Callable | None, Any, Any]:
    """Наполнение файла переменных окружения для allure-отчета."""
    environment_properties = {}

    def maker(key: str, value: str) -> None:
        environment_properties.update({key: value})

    yield maker

    alluredir = request.config.getoption('--alluredir')
    if not alluredir or not Path(alluredir).is_dir() or not environment_properties:
        return
    allure_env_path = Path(alluredir, 'environment.properties')
    with Path.open(allure_env_path, 'w', encoding='utf-8') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)


@allure.title('Загрузка переменных браузера')
@pytest.fixture(scope='session')
def browser_data(variables: dict) -> Generator[BrowserData, Any, None]:
    """Загрузка переменных браузера."""
    try:
        yield BrowserData(
            name=variables['browser']['name'],
            version=variables['browser']['version'],
            cli_args=variables['browser'].setdefault('cli-arguments', []),
            prefs=variables['browser'].setdefault('prefs', []),
            page_load_strategy=variables['browser'].setdefault('page_load_strategy', 'normal'),
            accept_insecure_certs=variables['browser'].setdefault('accept_insecure_certs', False),
            unhandled_prompt_behavior=variables['browser'].setdefault(
                'unhandled_prompt_behavior',
                'dismiss and notify',
            ),
        )
    except KeyError as k:
        sys.exit(f'Отсутствует секция {k.args[0]} в файле данных браузера')
