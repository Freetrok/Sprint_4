
from pages.home_page import YaScooterHomePage
import allure
from utils.urls import Urls
from utils.locators import YaScooterHomePageLocator
from utils.test_data import YaScooterHomePageFAQ
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@allure.story('Тестирование домашней страницы')
class TestYaScooterHomePage:
    @allure.description('Нажатие на верхнюю кнопку заказа')
    def test_click_top_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_top_order_button()
        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.description('Нажатие на нижнюю кнопку заказа')
    def test_click_bottom_order_button_show_order_page(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_bottom_order_button()

        assert ya_scooter_home_page.current_url() == Urls.ORDER_PAGE

    @allure.description('Перейти на страницу Яндекса/Дзена')
    def test_click_yandex_button_go_to_yandex(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_yandex_button()
        ya_scooter_home_page.switch_window(1)
        ya_scooter_home_page.wait_url_until_not_about_blank()
        current_url = ya_scooter_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url)

    @allure.description('Отобразить ответ на первый вопрос')
    def test_faq_click_first_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element0 = driver.find_element(By.ID, "accordion__heading-0")
        driver.execute_script("arguments[0].scrollIntoView();", element0)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_0)))
        ya_scooter_home_page.click_faq_question(question_number=0)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=0))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer0

    @allure.description('Отобразить ответ на второй вопрос')
    def test_faq_click_second_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element1 = driver.find_element(By.ID, "accordion__heading-1")
        driver.execute_script("arguments[0].scrollIntoView();", element1)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_1)))
        ya_scooter_home_page.click_faq_question(question_number=1)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=1))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer1

    @allure.description('Отобразить ответ на третий вопрос')
    def test_faq_click_third_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element2 = driver.find_element(By.ID, "accordion__heading-2")
        driver.execute_script("arguments[0].scrollIntoView();", element2)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_2)))
        ya_scooter_home_page.click_faq_question(question_number=2)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=2))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer2

    @allure.description('Отобразить ответ на четвертый вопрос')
    def test_faq_click_fourth_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element3 = driver.find_element(By.ID, "accordion__heading-3")
        driver.execute_script("arguments[0].scrollIntoView();", element3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_3)))
        ya_scooter_home_page.click_faq_question(question_number=3)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=3))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer3

    @allure.description('Отобразить ответ на пятый вопрос')
    def test_faq_click_fifth_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element4 = driver.find_element(By.ID, "accordion__heading-4")
        driver.execute_script("arguments[0].scrollIntoView();", element4)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_4)))
        ya_scooter_home_page.click_faq_question(question_number=4)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=4))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer4

    @allure.description('Отобразить ответ на шестой вопрос')
    def test_faq_click_sixth_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element5 = driver.find_element(By.ID, "accordion__heading-5")
        driver.execute_script("arguments[0].scrollIntoView();", element5)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_1)))
        ya_scooter_home_page.click_faq_question(question_number=5)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=5))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer5

    @allure.description('Отобразить ответ на седьмой вопрос')
    def test_faq_click_seventh_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element6 = driver.find_element(By.ID, "accordion__heading-6")
        driver.execute_script("arguments[0].scrollIntoView();", element6)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_6)))
        ya_scooter_home_page.click_faq_question(question_number=6)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=6))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer6

    @allure.description('Отобразить ответ на восьмой вопрос')
    def test_faq_click_eighth_question_show_answer(self, driver):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.LIST_OF_QUESTIONS)))
        element7 = driver.find_element(By.ID, "accordion__heading-7")
        driver.execute_script("arguments[0].scrollIntoView();", element7)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((YaScooterHomePageLocator.QUESTION_7)))
        ya_scooter_home_page.click_faq_question(question_number=7)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.faq_answer(answer_number=7))

        assert answer.is_displayed() and answer.text == YaScooterHomePageFAQ.answer7
