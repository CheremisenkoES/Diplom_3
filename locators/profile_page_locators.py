from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Кнопка "Профиль"
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')

    # Кнопка "История заказов"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')