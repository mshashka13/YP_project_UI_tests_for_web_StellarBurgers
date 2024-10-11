# qa_python_sprint_5 

1. test_1_registration - Тесты на Регистрацию
   1) test_successful_registration - успешная регистрация при вводе валидных данных: Имя, Email, Пароль
   2) test_error_registration_empty_name - невозможность регистрации при незаполненном поле Имя
   3) test_error_registration_incorrect_email_form - невозможность регистрации при вводе email не в формате логин@домен
   4) test_error_registration_incorrect_password - невозможность регистрации и появление ошибки при вводе пароля длиной менее 6 символов

2. test_2_authorization - Тесты на Автоматизацию
   1) test_log_in_button_log_in_to_account_from_home_page - успешная авторизация по кнопке "Войти в аккаунт" на главной странице
   2) test_log_in_button_personal_account_from_home_page - успешная авторизация по кнопке "Личный кабинет" на главной странице
   3) test_log_in_button_login_from_registration_form - успешная авторизация по кнопке "Войти" в форме регистрации
   4) test_log_in_button_login_from_recover_password_form - успешная авторизация по кнопке "Войти" в форме восстановления пароля

3. test_3_go_to_personal_account - Тест на переход в личный кабинет
   1) test_click_to_personal_account - переход по кнопке "Личный кабинет" в профиль

4. test_4_go_from_personal_account_to_constructor - Тесты на переходы в конструктор из личного кабинета
   1) test_click_from_personal_account_to_home_page_click_constructor - переход по кнопке "Конструктор" из личного кабинета в конструктор
   2) test_click_from_personal_account_to_home_page_click_logo - переход в конструктор по клику на логотип

5. test_5_logout - Тест на выход из профиля по кнопке "Выйти"
   1) test_logout_button_log_out_from_personal_account - выход из профиля по кнопке "Выйти" в личном кабинете

6. test_6_constructor - Тесты переходов в разделе "Конструктор"
   1) test_class_sauces_before_click - отсутствие выделения раздела "Соусы"
   2) test_class_sauces_after_click - успешный переход в раздел "Соусы"
   3) test_class_topping_before_click - отсутствие выделения раздела "Начинки"
   4) test_class_topping_after_click - успешный переход в раздел "Начинки"
   5) test_class_bread_before_click - отсутствие выделения раздела "Булки"
   6) test_class_bread_after_click - успешный переход в раздел "Булки"
