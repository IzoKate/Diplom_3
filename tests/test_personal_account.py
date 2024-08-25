import allure

from constants import Constants
from page_object.personal_account import PersonalAccount
from page_object.recovery_password import RecoveryPage


@allure.epic('Проверка Личного кабинета')
class TestPersonalAccount:
    @allure.feature('Проверяем переход по кнопке Личный кабинет')
    def test_click_button_lk_go_personal_account(self, driver):
        personal_acc = PersonalAccount(driver)
        personal_acc.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        personal_acc.click_button_lk()
        assert driver.current_url == Constants.URL_LOGIN

    @allure.feature('Проверяем переход в раздел История заказов')
    def test_click_button_order_history_go_to_page_history(self, login):
        history_order = PersonalAccount(login)
        history_order.click_button_lk()
        history_order.wait_page(Constants.URL_PERSONAL_ACCOUNT)
        history_order.click_button_order_history()
        history_order.wait_page(Constants.URL_ORDER_HISTORY)


        assert login.current_url == Constants.URL_ORDER_HISTORY


    @allure.feature('Проверяем выход из аккаунта')
    def test_click_button_out_personal_account_logout(self, login):
        history_order = PersonalAccount(login)
        history_order.click_button_lk()
        history_order.wait_page(Constants.URL_PERSONAL_ACCOUNT)
        history_order.click_button_logout()
        history_order.wait_page(Constants.URL_LOGIN)
        assert login.current_url == Constants.URL_LOGIN

