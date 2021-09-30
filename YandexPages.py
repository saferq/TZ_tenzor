from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json


class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELDS = (By.CLASS_NAME, "input__control")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CLASS_NAME, "service__name")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup")
    LOCATOR_YANDEX_LINKS_RESULT = (By.CLASS_NAME, "organic__url")
    LOCATOR_YANDEX_NAVIGATION_IMAGE = (By.XPATH, "//a[@data-id='images']")
    LOCATOR_YANDEX_FIRST_CATEGORY_IMAGE = (
        By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    LOCATOR_YANDEX_FIRST_CATEGORY_IMAGE_TEXT = (
        By.CLASS_NAME, "PopularRequestList-SearchText")
    LOCATOR_YANDEX_PAGE_DATA_STATE = (By.XPATH, "//div[@data-state]")
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CLASS_NAME, "serp-item_pos_0")
    LOCATOR_YANDEX_IMAGE_BUTTON_NEXT = (
        By.CLASS_NAME, "CircleButton_type_next")
    LOCATOR_YANDEX_IMAGE_BUTTON_PREV = (
        By.CLASS_NAME, "CircleButton_type_prev")
    LOCATOR_YANDEX_CHECK_OPEN_IMAGE = (By.CLASS_NAME, "Modal_visible")
    LOCATOR_YANDEX_OPEN_IMAGE = (By.CLASS_NAME, "MMImage-Origin")


class SearchTenzor(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELDS)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def input_enter(self):
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELDS, time=2).send_keys(Keys.RETURN)

    def check_search_field(self):
        return self.check_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELDS, time=5)

    def check_suggest(self):
        return self.check_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST, time=5)

    def get_and_check_urls(self, url):
        elements = self.find_elements(
            YandexSearchLocators.LOCATOR_YANDEX_LINKS_RESULT, time=5)
        links = [elem.get_attribute('href') for elem in elements]
        check_search_results = False
        for s in filter(lambda x: url in x, links): check_search_results = True
        return check_search_results


class ImageYandex(BasePage):
    def get_url_image(self):
        ''' Получает ссылку «Картинки» '''
        return self.get_value_attribute(
            YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_IMAGE)

    def click_to_link_image(self):
        ''' Кликает на ссылку «Картинки» '''
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_NAVIGATION_IMAGE, time=5).click()

    def switch_window(self):
        ''' Переходит на другую вкладку '''
        return self.switch_to_window()

    def get_text_first_category(self):
        ''' Получает текст первой категории '''
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY_IMAGE_TEXT, time=5).text

    def open_first_category(self):
        ''' Открывает 1 категорию '''
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY_IMAGE, time=5).click()

    def get_text_search_image(self):
        ''' Получает текст поиского запроса '''
        date_state = self.get_value_attribute(
            YandexSearchLocators.LOCATOR_YANDEX_PAGE_DATA_STATE, "data-state", time=5)
        date_dict = json.loads(date_state.replace("'", "\""))
        return date_dict['requests'][0]['text']

    def open_first_image(self):
        ''' Открывает 1 картинку '''
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=5).click()

    def check_open_image(self):
        ''' Проверяет открытие изображения '''
        return self.check_element(
            YandexSearchLocators.LOCATOR_YANDEX_CHECK_OPEN_IMAGE, time=5)

    def get_url_open_image(self):
        ''' Получает URL открытого сообщения '''
        return self.get_value_attribute(
            YandexSearchLocators.LOCATOR_YANDEX_OPEN_IMAGE, 'src', time=5)

    def open_next_image(self):
        ''' Нажимает кнопку вперед '''
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_IMAGE_BUTTON_NEXT, time=5).click()

    def open_prev_image(self):
        ''' Нажимает кнопку назад '''
        return self.find_element(
            YandexSearchLocators.LOCATOR_YANDEX_IMAGE_BUTTON_PREV, time=5).click()
