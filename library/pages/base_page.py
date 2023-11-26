import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def do_click(self, locator: [str, str]) -> None:
        """Нажатие на элемент"""
        with allure.step(f'Нажатие на элемент по локатору {locator}'):
            self.wait_element_to_be_clickable(locator=locator).click()

    def do_send_keys(self, locator: [str, str], text: str) -> None:
        """Отправка последовательности символов в элемент"""
        with allure.step(f'Отправка последовательности символов в элемент по локатору {locator}'):
            self.wait_visibility_of_element_located(locator=locator).send_keys(text)

    def get_title(self) -> str:
        """Получение заголовка страницы"""
        with allure.step('Получение заголовка страницы'):
            return self.driver.title

    def scroll_to_bottom(self) -> None:
        """Прокручивание страницы вниз до конца"""
        with allure.step('Прокручивание страницы вниз до конца'):
            self.driver.execute_script('')

    def get_element_text(self, locator: [str, str]) -> str:
        """Получение текста элемента"""
        with allure.step(f'Получение текста элемента по локатору {locator}'):
            return self.wait_visibility_of_element_located(locator=locator).text

    def wait_visibility_of_element_located(self, locator: tuple[str, str], timeout: int | None = None) -> WebElement:
        """Ожидание видимости элемента по локатору"""
        with allure.step(f'Ожидание видимости элемента по локатору {locator}'):
            # TODO: обработка использования ignored_exceptions
            ignored_exceptions = []
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=ignored_exceptions).until(
                ec.visibility_of_element_located(locator))

    def wait_element_to_be_clickable(self, locator: tuple[str, str], timeout: int | None = None) -> WebElement:
        """Ожидание видимости элемента по локатору"""
        with allure.step(f'Ожидание видимости элемента по локатору {locator}'):
            # TODO: обработка использования ignored_exceptions
            ignored_exceptions = []
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=ignored_exceptions).until(
                ec.element_to_be_clickable(locator))

    def wait_url_changes(self, url: str, timeout: int | None = None) -> bool:
        """Ожидание изменения URL"""
        with allure.step('Ожидание изменения URL'):
            ignored_exceptions = []
            timeout = timeout or self.timeout
            return WebDriverWait(self.driver, timeout, ignored_exceptions=ignored_exceptions).until(ec.url_changes(url))
