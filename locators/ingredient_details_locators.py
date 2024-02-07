from selenium.webdriver.common.by import By


class IngredientDetailsLocators:
    # Хедер "Детали ингредиента"
    DETAILS_HEADER = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    # Кнопка Закрыть
    CLOSE_BUTTON = (By.XPATH, '//section[contains(@class,"opened")]//button')