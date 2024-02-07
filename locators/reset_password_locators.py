from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    # Поле ввода пароля
    PASSWORD_FIELD = (By.XPATH, '//fieldset[1]//div[contains(@class,"input_size_default")]')

    # Кнопка "Показать пароль"
    SHOW_BUTTON = (By.XPATH, '//div[contains(@class,"input__icon")]/*')
