from YandexPages import ImageYandex, SearchTenzor


def test_tenzor_search(browser):
    yandex_main_page = SearchTenzor(browser)
    # 1) Зайти на yandex.ru
    yandex_main_page.go_to_site()
    # 2) Проверить наличия поля поиска
    assert yandex_main_page.check_search_field()
    # 3) Ввести в поиск Тензор
    yandex_main_page.enter_word("Тензор")
    # 4) Проверить, что появилась таблица с подсказками (suggest)
    assert yandex_main_page.check_suggest()
    # 5) При нажатии Enter появляется таблица результатов поиска
    yandex_main_page.input_enter()
    # 6) В первых 5 результатах есть ссылка на tensor.ru
    assert yandex_main_page.get_and_check_urls('tensor.ru')


def test_yandex_image(browser):
    # 1) Зайти на yandex.ru
    main_page = ImageYandex(browser)
    main_page.go_to_site()
    # 2) Ссылка «Картинки» присутствует на странице
    url_image = main_page.get_url_image()
    assert 'https://yandex.ru/images/' in url_image
    # 3) Кликаем на ссылку «Картинки»
    main_page.click_to_link_image()
    # 4) Проверить, что перешли на url https://yandex.ru/images/
    page = main_page.switch_window()
    assert 'https://yandex.ru/images/' in page.current_url
    # 5) Открыть 1 категорию, проверить что открылась, в поиске верный текст
    text_category = main_page.get_text_first_category()
    main_page.open_first_category()
    text_in_search = main_page.get_text_search_image()
    assert text_category == text_in_search
    # 6) Открыть 1 картинку, проверить что открылась
    main_page.open_first_image()
    assert main_page.check_open_image()
    url_first_image = main_page.get_url_open_image()
    # 7) При нажатии кнопки вперед картинка изменяется
    main_page.open_next_image()
    url_second_image = main_page.get_url_open_image()
    assert url_first_image != url_second_image
    # 8) При нажатии кнопки назад картинка изменяется на изображение из шага 6.
    #    Необходимо проверить, что это то же изображение.
    main_page.open_prev_image()
    url_third_image = main_page.get_url_open_image()
    assert url_first_image == url_third_image
