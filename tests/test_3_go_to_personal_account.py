from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestClickPersonalAccount:

    def test_click_to_personal_account(self, authorization):
        authorization.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        personal_account_page = authorization.find_element(*TestLocators.SEARCH_ELEMENT_PROFILE)
        assert personal_account_page.text == 'Профиль'
