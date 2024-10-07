from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestConstructor:

    def test_go_to_sections_bread_sauces_topping(self, driver):

        URL = "https://stellarburgers.nomoreparties.site/"
        driver.get(URL)

        element_sauces = driver.find_element(*TestLocators.SEARCH_ELEMENT_SAUCES)
        class_sauces_before_click = element_sauces.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" not in class_sauces_before_click

        element_sauces.click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_SELECTED_ELEMENT))
        class_sauces_after_click = element_sauces.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in class_sauces_after_click



        element_topping = driver.find_element(*TestLocators.SEARCH_ELEMENT_TOPPING)
        class_topping_before_click = element_topping.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" not in class_topping_before_click

        element_topping.click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_SELECTED_ELEMENT))
        class_topping_after_click = element_topping.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in class_topping_after_click



        element_bread = driver.find_element(*TestLocators.SEARCH_ELEMENT_BREAD)
        class_bread_before_click = element_bread.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" not in class_bread_before_click

        element_bread.click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SEARCH_SELECTED_ELEMENT))
        class_bread_after_click = element_bread.get_attribute("class")
        assert "tab_tab_type_current__2BEPc" in class_bread_after_click
