from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestLogout:

    def test_logout_button_log_out_from_personal_account(self, authorization):
        URL_HOME_PAGE = "https://stellarburgers.nomoreparties.site/"
        URL_LOG_IN = "https://stellarburgers.nomoreparties.site/login"
        assert authorization.current_url == URL_HOME_PAGE

        authorization.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(authorization, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))

        personal_account_page = authorization.find_element(By.XPATH, "//a[text()='Профиль']")
        assert personal_account_page.text == 'Профиль'

        authorization.find_element(By.XPATH, "//button[text()='Выход']").click()
        WebDriverWait(authorization, 5).until(EC.url_to_be(URL_LOG_IN))
        assert authorization.current_url == URL_LOG_IN
