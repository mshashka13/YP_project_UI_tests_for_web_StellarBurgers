from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestAuthorization:

    def test_log_in_button_log_in_to_account_from_home_page(self, driver):
        URL_HOME_PAGE = "https://stellarburgers.nomoreparties.site/"

        driver.get(URL_HOME_PAGE)

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))

        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys("maria_shasha_14qa_111@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys("123456")
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(URL_HOME_PAGE)))

        assert driver.current_url == URL_HOME_PAGE

    def test_log_in_button_personal_account_from_home_page(self, driver):
        URL_HOME_PAGE = "https://stellarburgers.nomoreparties.site/"

        driver.get(URL_HOME_PAGE)

        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))

        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys("maria_shasha_14qa_111@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys("123456")
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(URL_HOME_PAGE)))

        assert driver.current_url == URL_HOME_PAGE

    def test_log_in_button_login_from_registration_form(self, driver):
        URL_FORM_REGISTRATION = "https://stellarburgers.nomoreparties.site/register"
        URL_HOME_PAGE = "https://stellarburgers.nomoreparties.site/"

        driver.get(URL_FORM_REGISTRATION)

        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))

        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys("maria_shasha_14qa_111@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys("123456")
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(URL_HOME_PAGE)))

        assert driver.current_url == URL_HOME_PAGE

    def test_log_in_button_login_from_recover_password_form(self, driver):
        URL_FORM_RECOVER_PASSWORD = "https://stellarburgers.nomoreparties.site/reset-password"
        URL_HOME_PAGE = "https://stellarburgers.nomoreparties.site/"

        driver.get(URL_FORM_RECOVER_PASSWORD)

        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_INPUT_EMAIL_LOG_IN))

        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys("maria_shasha_14qa_111@ya.ru")
        driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys("123456")
        driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
        WebDriverWait(driver, 5).until((EC.url_to_be(URL_HOME_PAGE)))

        assert driver.current_url == URL_HOME_PAGE


