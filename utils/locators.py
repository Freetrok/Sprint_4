from selenium.webdriver.common.by import By


class BasePageLocator:
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    YANDEX_SITE_BUTTON = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]
    ORDER_STATUS_INPUT_ORDER_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder='Введите номер заказа']"]
    GO_TO_ORDER_STATUS_PAGE = [By.XPATH, ".//button[text()='Go!']"]


class YaScooterHomePageLocator:
    TOP_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    FAQ_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]
    FAQ_ANSWERS = [By.CSS_SELECTOR, ".accordion__panel > p"]
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]
    LIST_OF_QUESTIONS = [By.CLASS_NAME, "Home_FAQ__3uVm4"]
    QUESTION_0 = [By.ID, "accordion__heading-0"]
    QUESTION_1 = [By.ID, "accordion__heading-1"]
    QUESTION_2 = [By.ID, "accordion__heading-2"]
    QUESTION_3 = [By.ID, "accordion__heading-3"]
    QUESTION_4 = [By.ID, "accordion__heading-4"]
    QUESTION_5 = [By.ID, "accordion__heading-5"]
    QUESTION_6 = [By.ID, "accordion__heading-6"]
    QUESTION_7 = [By.ID, "accordion__heading-7"]

    @staticmethod
    def faq_question_button(question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]

    @staticmethod
    def faq_answer(answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"]


class YaScooterOrderPageLocator:
    FIRST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    INCORRECT_FIRST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"]
    LAST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    INCORRECT_LAST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]/parent::div/div"]
    ADDRESS_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    INCORRECT_ADDRESS_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]/parent::div/div"]
    SUBWAY_FIELD = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]
    INCORRECT_SUBWAY_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'метро')]/parent::div/parent::div/parent::div/div[@class!='select-search']"]

    @staticmethod
    def subway_hint_button(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]

    TELEPHONE_NUMBER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    INCORRECT_TELEPHONE_NUMBER_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]/parent::div/div"]

    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    BACK_BUTTON = [By.XPATH, ".//button[text()='Назад']"]
    DATE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    COMMENT_FOR_COURIER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_COMPLETED_INFO = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    SHOW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]


class YaScooterTrackPageLocator:
    MAIN_ORDER_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder='']"]


class YandexPageLocator:
    DOWNLOAD_BUTTON = [By.XPATH, ".//a[text='Установить']"]