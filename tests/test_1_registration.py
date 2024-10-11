from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constans import Constans


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(Constans.URL_REGISTRATION)
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys(Constans.NAME_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(Constans.RANDOM_EMAIL)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(Constans.RANDOM_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_AUTHORIZATION)))
        assert driver.current_url == Constans.URL_AUTHORIZATION

    def test_error_registration_empty_name(self, driver):
        driver.get(Constans.URL_REGISTRATION)
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys("")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(Constans.RANDOM_EMAIL)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(Constans.RANDOM_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_REGISTRATION)))
        button_registration = driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION)
        assert button_registration is not None

    def test_error_registration_incorrect_email_form(self, driver):
        driver.get(Constans.URL_REGISTRATION)
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys(Constans.NAME_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys("qa")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(Constans.RANDOM_PASSWORD)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_REGISTRATION)))
        button_registration = driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION)
        assert button_registration is not None

    def test_error_registration_incorrect_password(self, driver):
        driver.get(Constans.URL_REGISTRATION)
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys(Constans.NAME_USER)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(Constans.RANDOM_EMAIL)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234")
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_REGISTRATION)))
        error_password = driver.find_element(*TestLocators.SEARCH_ERROR_PASSWORD)
        assert error_password.is_displayed()