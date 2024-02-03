from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    # Кнопка "Выход"
    EXIT_BUTTON = (By.XPATH, '//button[(text()="Выход")]')

    # Активированная кнопка "История заказов"
    ENABLED_ORDER_HISTORY_BUTTON = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')