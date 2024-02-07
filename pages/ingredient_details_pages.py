import allure
from locators.ingredient_details_locators import IngredientDetailsLocators
from pages.base_page import BasePage


class IngredientDetailsPage(BasePage):
    @allure.step('Тест появления поп-апа с деталями')
    def check_show_window_with_details(self):
        self.wait_for_visibility_of_element(IngredientDetailsLocators.DETAILS_HEADER)
        return self.get_actually_text(IngredientDetailsLocators.DETAILS_HEADER)

    @allure.step('Клик по Х')
    def click_close_button(self):
        self.click_on_element(IngredientDetailsLocators.CLOSE_BUTTON)

    @allure.step('Тест закрытия поп-апа')
    def check_window_closed(self):
        self.wait_for_invisibility_of_element(IngredientDetailsLocators.DETAILS_HEADER)
        return self.element_displayed(IngredientDetailsLocators.DETAILS_HEADER)