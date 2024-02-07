from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Хедер "Лента заказов"
    ORDER_FEED_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')

    # Заказ
    ORDER = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]')

    # Всплывающее окно с деталями
    POP_UP_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_order")]')

    # Номера всех заказов в ленте
    ORDER_NUMBERS = (By.XPATH, '//p[@class="text text_type_digits-default"]')

    # Номер последнего заказа в ленте
    LAST_ORDER = (By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]')

    # Счётчик "Выполнено за всё время"
    ALL_TIME_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "digits")]')

    # Счётчик "Выполнено за сегодня"
    TODAY_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class, "digits")]')

    # Номер в разделе "В работе"
    NUMBER_IN_PROGRESS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')