from pages.base_page import BasePage
from utils.locators import YaScooterHomePageLocator as Locators
from utils.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.test_data import YaScooterHomePageFAQ as YaFAQ
import allure


class YaScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS, 10)
        return elems[question_number].click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Выполнить прокрутку')
    def scroll_faq_question(self):
        return self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(Locators.QUESTION_7))


    @allure.step('Кликнуть по вопросу')
    def click_faq_question(self, question: int):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(Locators.QUESTION_7))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.QUESTION_7))
        method, locator = Locators.change_questions
        locator = locator.format(question)
        element = self.driver.find_element(method, locator)
        return element.click()

    @allure.step('Получить текст ответа')
    def take_faq_answer(self, answer: int):
        method, locator = Locators.change_answers
        locator = locator.format(answer)
        element = self.driver.find_element(method, locator)
        return element

    @allure.step('Перейти на страницу Яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.YANDEX_SITE_BUTTON).click()