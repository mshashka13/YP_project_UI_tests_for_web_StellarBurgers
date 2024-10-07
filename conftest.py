import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    URL_LOG_IN_FIXTURE = "https://stellarburgers.nomoreparties.site/login"
    URL_HOME_PAGE_FIXTURE = "https://stellarburgers.nomoreparties.site/"
    driver.get(URL_LOG_IN_FIXTURE)

    driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys("maria_shasha_14qa_111@ya.ru")
    driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys("123456")
    driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
    WebDriverWait(driver, 5).until((EC.url_to_be(URL_HOME_PAGE_FIXTURE)))

    yield driver

@pytest.fixture
def random_email():
    email = f"maria_shasha_14qa{random.randint(111, 999)}@yandex.ru"
    return email

@pytest.fixture
def random_password():
    password = f"{random.randint(111111, 999999)}"
    return password
