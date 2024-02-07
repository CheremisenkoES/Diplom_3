import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на кнопку «Личный кабинет»')
    def click_personal_account_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку «Лента Заказов»')
    def click_order_feed_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Тест перехода на главную страницу')
    def check_switch_on_main_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.BURGER_HEADER)
        return self.get_current_url()

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainPageLocators.COUNTER)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step('Клик на кнопку «Оформить заказ»')
    def click_checkout_button(self):
        self.click_on_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step('Проверка появление ID заказа после оформления')
    def check_show_window_with_order_id(self):
        self.wait_for_visibility_of_element(MainPageLocators.ORDER_ID)
        return self.get_actually_text(MainPageLocators.ORDER_ID)