from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constans import Constans


class TestLogout:

    def test_logout_button_log_out_from_personal_account(self, authorization):
        authorization.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        authorization.find_element(*TestLocators.SEARCH_ELEMENT_LOGOUT).click()
        WebDriverWait(authorization, 5).until(EC.invisibility_of_element_located(TestLocators.SEARCH_ELEMENT_PROFILE))
        assert authorization.current_url == Constans.URL_AUTHORIZATION
