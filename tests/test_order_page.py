import pytest

from pages.order_page import YaScooterOrderPage
from pages.home_page import YaScooterHomePage
import allure
from utils.urls import Urls
from utils.locators import YaScooterOrderPageLocator
from utils.test_data import YaScooterOrderPageData as order_data


@allure.story('Тестирование страницы оформления заказа')
class TestYaScooterOrderPage:
    @allure.description('Некорректное Имя')
    @allure.title('Проверка отображения ошибки при вводе некорректного имени')
    def test_order_page_first_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_first_name('Qwe')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_FIRST_NAME_MESSAGE).is_displayed(), "Ошибка при вводе некорректного имени не отображается!"

    @allure.description('Некорректная фамилия')
    @allure.title('Проверка отображения ошибки при вводе некорректной фамилии')
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_last_name('Qwe')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_LAST_NAME_MESSAGE).is_displayed(), "Ошибка при вводе некорректной фамилии не отображается!"

    @allure.description('Некорректный адрес')
    @allure.title('Проверка отображения ошибки при вводе некорректного адреса')
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_address('Qwe')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_ADDRESS_MESSAGE).is_displayed(), "Ошибка при вводе некорректного адреса не отображается!"

    @allure.description('Не указана станция метро')
    @allure.title('Проверка отображения ошибки при отсутствии выбранной станции метро')
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_SUBWAY_MESSAGE).is_displayed(), "Ошибка при отсутствии выбранной станции метро не отображается!"

    @allure.description('Некорректный номер телефона')
    @allure.title('Проверка отображения ошибки при вводе некорректного номера телефона')
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.input_telephone_number('Qwe')
        ya_scooter_order_page.go_next()
        assert ya_scooter_order_page.find_element(YaScooterOrderPageLocator.INCORRECT_TELEPHONE_NUMBER_MESSAGE).is_displayed(), "Ошибка при вводе некорректного номера телефона не отображается!"

    @allure.description('Заполнить данные на этапе "Для кого самокат" и перейти на этап "Про аренду"')
    @allure.title('Проверка корректности перехода на этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets['data_set1'])
        ya_scooter_order_page.go_next()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_BUTTON)) > 0, "Переход на этап 'Про аренду' отсутствует"

    @allure.description('Заполнить данные на этапе "Про аренду" и оформить заказ')
    @allure.title('Проверка успешного оформления заказа на двух наборах данных')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        assert len(ya_scooter_order_page.find_elements(YaScooterOrderPageLocator.ORDER_COMPLETED_INFO)) > 0, "Ошибка. Заказ не оформлен"

    @allure.description('Заполнить данные на этапе "Про аренду", оформить заказ и перейти на статус заказа')
    @allure.title('Проверка успешного перехода к заказу после оформления заказа на двух наборах данных')
    @pytest.mark.parametrize('data_set', ['data_set1', 'data_set2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_order_page.go_to_site(Urls.ORDER_PAGE)
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_order_page.fill_user_data(order_data.data_sets[data_set])
        ya_scooter_order_page.go_next()
        ya_scooter_order_page.fill_rent_data(order_data.data_sets[data_set])
        ya_scooter_order_page.click_order()
        ya_scooter_order_page.click_accept_order()
        order_number = ya_scooter_order_page.get_order_number()
        ya_scooter_order_page.click_go_to_status()
        current_url = ya_scooter_order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url), "Ошибка. Переход к оформленному заказу отсутствует."