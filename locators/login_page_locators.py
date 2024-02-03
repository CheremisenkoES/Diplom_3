from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Ссылка "Восстановить пароль"
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, 'Восстановить пароль')

    # Поле для email
    EMAIL = (By.NAME, 'name')

    # Поле для пароля
    PASSWORD = (By.NAME, 'Пароль')

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, '//button[(text()="Войти")]')

    # Хедер "Вход"
    LOGIN_HEADER = (By.XPATH, '.// h2[text() = "Вход"]')