import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedLocators


@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.title('Тест появления всплывающего окна с деталями заказа')
    @allure.description('Всплывающее окно с деталями появляется по клику')
    def test_popup_details_after_click_on_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_order()
        displayed = order_feed_page.check_show_window_with_details()
        assert displayed

    @allure.title('Тест отображения заказов пользователя в Ленте заказов')
    @allure.description('Заказы в разделе «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_in_feed_orders(self, authorization, orders_numbers):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        feed_orders = order_feed_page.get_orders_numbers(orders_numbers)
        assert set(map(str, orders_numbers)).issubset(set(feed_orders))

    @allure.title('Тест увеличения счетчика заказов после создания нового заказа')
    @allure.description('Проверка значение счетчика до и после создания нового заказа + общее число')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.ALL_TIME_COUNTER, OrderFeedLocators.TODAY_COUNTER])
    def test_order_counter_today_and_all_time_value(self, user_data, authorization, counter):
        driver = authorization
        payload, token = user_data
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        prev_counter_value = order_feed_page.get_counter_value(counter)
        order_feed_page.create_order(token)
        current_counter_value = order_feed_page.get_counter_value(counter)
        assert current_counter_value >= prev_counter_value

    @allure.title('Тест отображения номера заказа в разделе "В работе')
    @allure.description('После оформления, номер заказа появляется в разделе "В работе"')
    def test_show_order_number_in_progress(self, authorization, orders_numbers):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        last_order = order_feed_page.get_user_order(orders_numbers)
        order_in_progress = order_feed_page.get_user_order_in_progress()
        assert last_order == order_in_progress