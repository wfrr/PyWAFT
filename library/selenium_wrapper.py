from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWebDriver
from selenium import webdriver


def init_chrome(browser_version: str) -> ChromeWebDriver:
    options = ChromeOptions()
    options.browser_version = browser_version
    return webdriver.Chrome(options=options)


def init_firefox(browser_version: str) -> FirefoxWebDriver:
    options = FirefoxOptions()
    options.browser_version = browser_version
    return webdriver.Firefox(options=options)


def init_edge(browser_version: str) -> EdgeWebDriver:
    options = EdgeOptions()
    options.browser_version = browser_version
    return webdriver.Edge(options=options)
