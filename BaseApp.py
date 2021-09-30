from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def check_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")
        except exceptions.NoSuchElementException:
            return False
        return True

    def switch_to_window(self, time=10):
        ''' Переходит на другую вкладку '''
        page_first = self.driver.current_window_handle
        page_next = self.driver.window_handles
        new_page = [x for x in page_next if x != page_first][0]
        self.driver.switch_to.window(new_page)
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable((By.XPATH, "//div")))
        return self.driver

    def get_value_attribute(self, locator, attribute='href', time=10):
        ''' Получает значение href элемента  '''
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")
        return element.get_attribute(attribute)
