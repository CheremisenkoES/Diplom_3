from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    # Хедер "Восстановление пароля"
    PASSWORD_RECOVERY_HEADER = (By.XPATH,'.//h2[text() = "Восстановление пароля"]')

    # Поле "email"
    EMAIL_FIELD = (By.TAG_NAME, 'input')

    # Кнопка "Восстановить"
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')