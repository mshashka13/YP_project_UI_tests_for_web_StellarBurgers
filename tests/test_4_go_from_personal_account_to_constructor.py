from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constans import Constans


class TestClickFromPersonalAccount:

    def test_click_from_personal_account_to_home_page_click_constructor(self, authorization):
        authorization.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        authorization.find_element(*TestLocators.SEARCH_ELEMENT_CONSTRUCTOR).click()
        assert authorization.current_url == Constans.URL_HOME_PAGE

    def test_click_from_personal_account_to_home_page_click_logo(self, authorization):
        authorization.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_PERSONAL_ACCOUNT).click()
        WebDriverWait(authorization, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        authorization.find_element(*TestLocators.SEARCH_LOGO_STELLAR_BURGERS).click()
        assert authorization.current_url == Constans.URL_HOME_PAGE
