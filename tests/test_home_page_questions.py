import pytest
from pages.home_page import YaScooterHomePage
from utils.test_data import YaScooterHomePageFAQ as YaFAQ
import allure

@allure.story('Тестирование вопросов в разделе FAQ на главной')
class TestQuestionsHoomePage:
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
        test_questions_home_page = YaScooterHomePage(driver)
        test_questions_home_page.go_to_site()
        test_questions_home_page.click_cookie_accept()
        test_questions_home_page.scroll_faq_question()
        test_questions_home_page.click_faq_question(question)
        test_questions_home_page.take_faq_answer(answer)
        answer = test_questions_home_page.take_faq_answer(answer)
        assert answer.is_displayed() and answer.text == YaFAQ.answer[answer_text], f"Некорректно отображается ответ на вопрос {question}!"