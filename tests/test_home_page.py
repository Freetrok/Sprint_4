import pytest
from pages.home_page import YaScooterHomePage
from utils.test_data import YaScooterHomePageFAQ as YaFAQ
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
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.description('Нажатие на нижнюю кнопку заказа')
    @allure.title('Проверка успешного входа в форму заказа через нижнюю кнопку заказа')
    def test_click_bottom_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

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

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url)


    @allure.description('Отобразить ответы на вопросы с 1 по 8')
    @allure.title('Проверка корректного отображения ответов на вопросы в разделе FAQ')
    @pytest.mark.parametrize('question, answer, answer_text',
                             [['0', '0', 'answer0'],
                              ['1', '1', 'answer1'],
                             ['2', '2', 'answer2'],
                             ['3', '3', 'answer3'],
                             ['4', '4', 'answer4'],
                             ['5', '5', 'answer5'],
                             ['6', '6', 'answer6'],
                             ['7', '7', 'answer7']])
    def test_click_questions_show_answers(self, driver, question, answer, answer_text):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.scroll_faq_question()
        ya_scooter_home_page.click_faq_question(question)
        ya_scooter_home_page.take_faq_answer(answer)
        answer = ya_scooter_home_page.take_faq_answer(answer)
        assert answer.is_displayed() and answer.text == YaFAQ.answer[answer_text]