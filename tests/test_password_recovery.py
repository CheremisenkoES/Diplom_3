import allure
from pages.forgot_pass_page import ForgotPasswordPage
from pages.reset_pass_page import ResetPasswordPage
from data.forgot_password_constants import ForgotPasswordConstants
from data.urls_constants import UrlsConstants

@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description(
        'Переход на страницу восстановления пароля'
    )
    def test_transfer_to_page_password_recovery(self, password_recovery):
        driver = password_recovery
        forgot_pass_page = ForgotPasswordPage(driver)
        current_url = forgot_pass_page.check_switch_on_forgot_pass()
        assert current_url == ForgotPasswordConstants.FORGOT_PASS_URL

    @allure.title('Тест клика по кнопке «Восстановить»')
    @allure.description('Ввод почты и клик по кнопке «Восстановить»,')
    def test_enter_email_and_click_password_recover_button(self, forgot_pass_page):
        driver = forgot_pass_page
        reset_pass_page = ResetPasswordPage(driver)
        current_url = reset_pass_page.check_switch_on_reset_pass()
        assert current_url == UrlsConstants.RESET_PASS_URL

    @allure.title('Тест клика по кнопке показать/скрыть пароль')
    @allure.description('Пароль скрывается и появляется. Поле делается активным')
    def test_click_show_password_button_and_field_active(self, forgot_pass_page):
        driver = forgot_pass_page
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.click_show_button()
        class_value = reset_pass_page.check_pass_field_active()
        assert 'status_active' in class_value