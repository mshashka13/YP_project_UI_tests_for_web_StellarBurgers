from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestRegistration:

    def test_successful_registration(self, driver, random_email, random_password):
        URL = "https://stellarburgers.nomoreparties.site/register"
        EXPECTED_URL = "https://stellarburgers.nomoreparties.site/login"


        driver.get(URL)

        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys("Мария")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until((EC.url_to_be(EXPECTED_URL)))

        assert driver.current_url == EXPECTED_URL

    def test_error_registration_empty_name(self, driver, random_email, random_password):
        URL = "https://stellarburgers.nomoreparties.site/register"

        driver.get(URL)

        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys("")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until((EC.url_to_be(URL)))

        assert driver.current_url == URL

    def test_error_registration_incorrect_email_form(self, driver, random_password):
        URL = "https://stellarburgers.nomoreparties.site/register"

        driver.get(URL)

        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys("Мария")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys("qa")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys(random_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until((EC.url_to_be(URL)))

        assert driver.current_url == URL

    def test_error_registration_incorrect_password(self, driver, random_email):

        URL = "https://stellarburgers.nomoreparties.site/register"
        driver.get(URL)

        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys("Мария")
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(random_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD).send_keys("1234")
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']")))
        error_password = driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")

        assert error_password.is_displayed()
        assert error_password.text == "Некорректный пароль"