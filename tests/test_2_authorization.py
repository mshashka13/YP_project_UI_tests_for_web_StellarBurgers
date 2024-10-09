from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constans import Constans


class TestAuthorization:

    def test_log_in_button_log_in_to_account_from_home_page(self, driver):
        driver.get(Constans.URL_HOME_PAGE)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_HOME_PAGE).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys(Constans.EMAIL_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys(Constans.PASSWORD_USER)
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_HOME_PAGE)))
        assert driver.current_url == Constans.URL_HOME_PAGE

    def test_log_in_button_personal_account_from_home_page(self, driver):
        driver.get(Constans.URL_HOME_PAGE)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys(Constans.EMAIL_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys(Constans.PASSWORD_USER)
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_HOME_PAGE)))
        assert driver.current_url == Constans.URL_HOME_PAGE

    def test_log_in_button_login_from_registration_form(self, driver):
        driver.get(Constans.URL_REGISTRATION)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_REGISTRATION_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys(Constans.EMAIL_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys(Constans.PASSWORD_USER)
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_HOME_PAGE)))
        assert driver.current_url == Constans.URL_HOME_PAGE

    def test_log_in_button_login_from_recover_password_form(self, driver):
        driver.get(Constans.URL_RECOVER_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_RECOVERY_PASSWORD_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys(Constans.EMAIL_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys(Constans.PASSWORD_USER)
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_HOME_PAGE)))
        assert driver.current_url == Constans.URL_HOME_PAGE


