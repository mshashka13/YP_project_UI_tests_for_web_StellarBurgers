from selenium.webdriver.common.by import By

class TestLocators:

    #Форма Регистрации
    SEARCH_INPUT_NAME = [By.XPATH, "//fieldset[1]/div/div/input"] #поле Имя
    SEARCH_INPUT_EMAIL = [By.XPATH, "//fieldset[2]/div/div/input"] #поле Email
    SEARCH_INPUT_PASSWORD = [By.XPATH, "//fieldset[3]/div/div/input"] #поле Пароль
    SEARCH_BUTTON_REGISTRATION = [By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"] #кнопка Зарегистрироваться
    SEARCH_ERROR_PASSWORD = [By.XPATH, "//p[text()='Некорректный пароль']"] #ошибка при некорректном пароле

    #Вход в форму авторизации
    SEARCH_BUTTON_LOG_IN_HOME_PAGE = [By.XPATH, "//button[text()='Войти в аккаунт']"] #кнопка Войти в аккаунт на главной странице
    SEARCH_BUTTON_LOG_IN_PERSONAL_ACCOUNT = [By.XPATH, "//p[text()='Личный Кабинет']"] #кнопка Личный кабинет
    SEARCH_BUTTON_LOG_IN_REGISTRATION_FORM = [By.XPATH, "//a[text()='Войти']"] #кнопка Войти в форме регистрации
    SEARCH_BUTTON_LOG_IN_RECOVERY_PASSWORD_FORM = [By.XPATH, "//a[text()='Войти']"] #кнопка Войти в форме восстановления пароля

    #Форма Авторизации
    SEARCH_INPUT_EMAIL_LOG_IN = [By.NAME, "name"] #поле Email
    SEARCH_INPUT_PASSWORD_LOG_IN = [By.NAME, "Пароль"] #поле Пароль
    SEARCH_BUTTON_AUTHORIZATION = [By.XPATH, "//button[contains(text(), 'Войти')]"] #кнопка Войти

    #Раздел Конструктор
    SEARCH_ELEMENT_BREAD = [By.XPATH, ".//section[1]/div[1]/div[1]"] #кнопка Булки
    SEARCH_ELEMENT_SAUCES = [By.XPATH, ".//section[1]/div[1]/div[2]"] #кнопка Соусы
    SEARCH_ELEMENT_TOPPING = [By.XPATH, ".//section[1]/div[1]/div[3]"] #кнопка Начинки
    SEARCH_SELECTED_ELEMENT = [By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc"] #выделенная кнопка в разделе

    #Личный кабинет
    SEARCH_ELEMENT_PROFILE = [By.XPATH, "//a[text()='Профиль']"] #кнопка Профиль
    SEARCH_ELEMENT_LOGOUT = [By.XPATH, "//button[text()='Выход']"] #кнопка Выход
    SEARCH_ELEMENT_CONSTRUCTOR = [By.XPATH, "//p[text()='Конструктор']"] #кнопка Конструктор
    SEARCH_LOGO_STELLAR_BURGERS = [By.XPATH, "/html/body/div/div/header/nav/div"] #логотип Stellar Burgers
