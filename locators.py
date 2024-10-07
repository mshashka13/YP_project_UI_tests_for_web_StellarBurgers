from selenium.webdriver.common.by import By

class TestLocators:

    #Форма Регистрации
    SEARCH_INPUT_NAME = [By.XPATH, "//fieldset[1]/div/div/input"] #поле Имя
    SEARCH_INPUT_EMAIL = [By.XPATH, "//fieldset[2]/div/div/input"] #поле Email
    SEARCH_INPUT_PASSWORD = [By.XPATH, "//fieldset[3]/div/div/input"] #поле Пароль
    SEARCH_BUTTON_REGISTRATION = [By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"] #кнопка Зарегистрироваться

    #форма Авторизации
    SEARCH_INPUT_EMAIL_LOG_IN = [By.NAME, "name"] #поле Email
    SEARCH_INPUT_PASSWORD_LOG_IN = [By.NAME, "Пароль"] #поле Пароль
    SEARCH_BUTTON_AUTHORIZATION = [By.XPATH, "//button[contains(text(), 'Войти')]"] #кнопка Войти

    #Раздел Конструктор
    SEARCH_ELEMENT_BREAD = [By.XPATH, ".//section[1]/div[1]/div[1]"] #кнопка Булки
    SEARCH_ELEMENT_SAUCES = [By.XPATH, ".//section[1]/div[1]/div[2]"] #кнопка Соусы
    SEARCH_ELEMENT_TOPPING = [By.XPATH, ".//section[1]/div[1]/div[3]"] #кнопка Начинки
    SEARCH_SELECTED_ELEMENT = [By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc"] #выделенная кнопка