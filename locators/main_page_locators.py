from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')

    # Кнопка "Лента Заказов"
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')

    # Хедер "Соберите бургер"
    BURGER_HEADER = (By.XPATH, '//h1[text()="Соберите бургер"]')

    # Ингредиент "Флюоресцентная булка R2-D3"
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')

    # Счетчик
    COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')

    # Корзина для конструктора
    CONSTRUCTOR_BASKET = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')

    # Кнопка "Оформить заказ"
    CHECKOUT_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    # ID заказа
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')