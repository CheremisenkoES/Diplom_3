import allure
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step('Тест перехода на страницу сброса пароля')
    def check_switch_on_reset_pass(self):
        self.wait_for_element_to_be_clickable(ResetPasswordLocators.SHOW_BUTTON)
        return self.get_current_url()

    @allure.step('Клик на кнопку «Показать пароль»')
    def click_show_button(self):
        self.click_on_element(ResetPasswordLocators.SHOW_BUTTON)

    @allure.step('Тест, что поле «пароль» стало активным')
    def check_pass_field_active(self):
        return self.get_attribute_value(ResetPasswordLocators.PASSWORD_FIELD, 'class')