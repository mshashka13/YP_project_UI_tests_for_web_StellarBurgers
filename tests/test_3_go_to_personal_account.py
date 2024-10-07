from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestClickPersonalAccount:

    def test_click_to_personal_account(self, authorization):
        URL_HOME_PAGE = "https://stellarburgers.nomoreparties.site/"
        assert authorization.current_url == URL_HOME_PAGE

        authorization.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(authorization, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))

        personal_account_page = authorization.find_element(By.XPATH, "//a[text()='Профиль']")
        assert personal_account_page.text == 'Профиль'

