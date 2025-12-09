"""Врапперы для работы с selenium."""

from selenium.webdriver import Chrome, Edge, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from library.core.browser_data import BrowserData


def init_chrome(browser_data: BrowserData) -> Chrome:
    """Инициализация веб-драйвера Chrome."""
    options = ChromeOptions()
    options.browser_version = browser_data.version
    options.page_load_strategy = browser_data.page_load_strategy
    options.accept_insecure_certs = browser_data.accept_insecure_certs
    options.unhandled_prompt_behavior = browser_data.unhandled_prompt_behavior
    for pref in browser_data.prefs:
        options.add_experimental_option("prefs", pref)
    for arg in browser_data.cli_args:
        options.add_argument(arg)
    browser = Chrome(options=options)
    # TODO: position и размер окна из конфига
    # browser.set_window_position(0, 0)
    # browser.set_window_size(1920, 1080)
    return browser


def init_firefox(browser_data: BrowserData) -> Firefox:
    """Инициализация веб-драйвера Firefox."""
    options = FirefoxOptions()
    options.browser_version = browser_data.version
    options.page_load_strategy = browser_data.page_load_strategy
    options.accept_insecure_certs = browser_data.accept_insecure_certs
    options.unhandled_prompt_behavior = browser_data.unhandled_prompt_behavior
    for pref in browser_data.prefs:
        for name, value in pref.items():
            options.set_preference(name, value)
    for arg in browser_data.cli_args:
        options.add_argument(arg)
    browser = Firefox(options=options)
    # browser.set_window_position(0, 0)
    # browser.set_window_size(1920, 1080)
    return browser


def init_edge(browser_data: BrowserData) -> Edge:
    """Инициализация веб-драйвера Edge."""
    options = EdgeOptions()
    options.browser_version = browser_data.version
    options.page_load_strategy = browser_data.page_load_strategy
    options.accept_insecure_certs = browser_data.accept_insecure_certs
    options.unhandled_prompt_behavior = browser_data.unhandled_prompt_behavior
    for pref in browser_data.prefs:
        options.add_experimental_option("prefs", pref)
    for arg in browser_data.cli_args:
        options.add_argument(arg)
    browser = Edge(options=options)
    # browser.set_window_position(0, 0)
    # browser.set_window_size(1920, 1080)
    return browser
