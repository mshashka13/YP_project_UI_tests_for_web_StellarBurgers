import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constans import Constans


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    driver.get(Constans.URL_AUTHORIZATION)
    driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL_LOG_IN).send_keys(Constans.EMAIL_USER)
    driver.find_element(*TestLocators.SEARCH_INPUT_PASSWORD_LOG_IN).send_keys(Constans.PASSWORD_USER)
    driver.find_element(*TestLocators.SEARCH_BUTTON_AUTHORIZATION).click()
    WebDriverWait(driver, 5).until((EC.url_to_be(Constans.URL_HOME_PAGE)))
    yield driver

