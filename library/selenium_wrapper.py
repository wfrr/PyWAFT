"""Врапперы для работы с selenium"""

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge


def init_chrome(browser_version: str) -> Chrome:
    """Инициализация вебдрайвера Chrome"""
    options = ChromeOptions()
    options.browser_version = browser_version
    return Chrome(options=options)


def init_firefox(browser_version: str) -> Firefox:
    """Инициализация вебдрайвера Firefox"""
    options = FirefoxOptions()
    options.browser_version = browser_version
    return Firefox(options=options)


def init_edge(browser_version: str) -> Edge:
    """Инициализация вебдрайвера Edge"""
    options = EdgeOptions()
    options.browser_version = browser_version
    return Edge(options=options)
