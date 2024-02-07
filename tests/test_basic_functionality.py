import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_details_pages import IngredientDetailsPage
from data.urls_constants import UrlsConstants
from data.main_page_constants import MainPageConstants
from data.ingredient_details_constants import IngredientDetailsConstants

@allure.feature('Проверка основного функционала')
class TestBasicFunctionality:
    @allure.title('Тест перехода по клику на «Конструктор»')
    @allure.description(
        'Переход на Конструктор'
    )
    def test_click_and_transfer_to_constructor(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_constructor_button()
        main_page = MainPage(driver)
        current_url = main_page.check_switch_on_main_page()
        assert current_url == MainPageConstants.MAIN_PAGE_URL

    @allure.title('Тест перехода по клику на «Лента заказов»')
    @allure.description(
        'Переход на "Лента заказов"'
    )
    def test_click_and_transfer_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        current_url = order_feed_page.check_switch_on_order_feed()
        assert current_url == UrlsConstants.ORDER_FEED_URL


    @allure.title('Тест появления всплывающего окна с деталями')
    @allure.description('Нажатие на ингредиент открывает поп-ап с деталями')
    def test_click_and_show_popup_detail_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_pages = IngredientDetailsPage(driver)
        actually_text = ingredient_details_pages.check_show_window_with_details()
        assert actually_text == IngredientDetailsConstants.WINDOW_HEADER

    @allure.title('Тест закрытия поп-апа по Х')
    @allure.description('Поп-ап закрывается по крестику')
    def test_click_x_and_close_popup_ingredients(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_pages = IngredientDetailsPage(driver)
        ingredient_details_pages.click_close_button()
        displayed = ingredient_details_pages.check_window_closed()
        assert not displayed

    @allure.title('Тест увеличения счётчика ингридиента при добавлении в заказ')
    @allure.description('Счетчик ингредиента увеличивается')
    def test_rise_counter_value_when_add_ingredient(self, driver):
        main_page = MainPage(driver)
        prev_counter_value = main_page.get_count_value()
        main_page.add_ingredient()
        current_counter_value = main_page.get_count_value()
        assert current_counter_value > prev_counter_value

    @allure.title('Тест оформления заказ авторизованного пользователя')
    @allure.description('Заказ авторизированного пользователя оформляется')
    def test_making_an_order_click_checkout_button_show_window_with_order_id(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_checkout_button()
        actually_text = main_page.check_show_window_with_order_id()
        assert actually_text == MainPageConstants.ORDER_ID