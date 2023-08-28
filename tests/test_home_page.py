from pages.home_page import YaScooterHomePage
import allure
from utils.urls import Urls

@allure.story('Тестирование домашней страницы')
class TestYaScooterHomePage:
    @allure.description('Нажатие на верхнюю кнопку заказа')
    @allure.title('Проверка успешного входа в форму заказа через верхнюю кнопку заказа')
    def test_click_top_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_top_order_button()
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE, "Верхняя кнопка заказа ведет на некорректный URL"

    @allure.description('Нажатие на нижнюю кнопку заказа')
    @allure.title('Проверка успешного входа в форму заказа через нижнюю кнопку заказа')
    def test_click_bottom_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE, "Нижняя кнопка заказа ведет на некорректный URL"

    @allure.description('Перейти на страницу Яндекса/Дзена')
    @allure.title('Проверка успешного перехода на страницу Яндекса/Дзена')
    def test_click_yandex_button_go_to_yandex(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_yandex_button()
        ya_scooter_home_page.switch_window(1)
        ya_scooter_home_page.wait_url_until_not_about_blank()
        current_url = ya_scooter_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url), "Ошибка при переходе на страницу Яндекса/Дзена. Некорректный URL."
