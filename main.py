from selenium import webdriver
from BaseApp import BasePage
from YandexPages import SearchTenzor, ImageYandex
from time import sleep, time


def browser():
    driver = webdriver.Firefox()
    return driver


def tenzor_search(browser):
    main_page = SearchTenzor(browser)
    # 1) Зайти на yandex.ru
    main_page.go_to_site()
    # 2) Проверить наличия поля поиска
    assert main_page.check_search_field()
    # 3) Ввести в поиск Тензор
    main_page.enter_word("Тензор")
    # 4) Проверить, что появилась таблица с подсказками (suggest)
    assert main_page.check_suggest()
    # 5) При нажатии Enter появляется таблица результатов поиска
    main_page.input_enter()
    # 6) В первых 5 результатах есть ссылка на tensor.ru
    assert main_page.get_and_check_urls('tensor.ru')


def image_in_yandex(browser):
    main_page = ImageYandex(browser)
    # 1) Зайти на yandex.ru
    main_page.go_to_site()
    # 2) Ссылка «Картинки» присутствует на странице
    print('https://yandex.ru/images/' in main_page.get_url_image())
    # 3) Кликаем на ссылку «Картинки»
    main_page.click_to_link_image()
    # 4) Проверить, что перешли на url https://yandex.ru/images/
    images_page = main_page.switch_window()
    print(images_page.current_url)
    # 5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
    text_category = main_page.get_text_first_category()
    main_page.open_first_category()
    text_in_search = main_page.get_text_search_image()
    print(text_category == text_in_search)
    # 6) Открыть 1 картинку, проверить что открылась
    main_page.open_first_image()
    print(main_page.check_open_image())
    # 7) При нажатии кнопки вперед картинка изменяется
    url_first_image = main_page.get_url_open_image()
    print(url_first_image)
    main_page.open_next_image()
    url_second_image = main_page.get_url_open_image()
    print(url_second_image)
    # 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6.
    #    Необходимо проверить, что это то же изображение.
    main_page.open_prev_image()
    url_third_image = main_page.get_url_open_image()
    print(url_third_image)

    sleep(1)


if __name__ == '__main__':
    # tenzor_search(browser())
    image_in_yandex(browser())
