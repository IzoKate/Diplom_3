import allure


from constants import Constants
from page_object.base_function import BaseFunction



@allure.epic('Проверка Базового функционала')
class TestBaseFunctional:

    @allure.feature('Переход по клику на кнопку Конструктор')
    def test_click_button_constructor_gp_to_main_page(self, driver):
        modal_win = BaseFunction(driver)
        modal_win.go_to_site_stellarburger(Constants.URL_LOGIN)
        modal_win.click_button_constructor()
        modal_win.wait_page(Constants.URL_MAIN_PAGE)
        assert driver.current_url == Constants.URL_MAIN_PAGE

    @allure.feature('Переход по клику на кнопку Лента заказов')
    def test_click_button_feed_orders_go_to_page_feed(self, driver):
        modal_win = BaseFunction(driver)
        modal_win.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        modal_win.click_button_orders_feed()
        modal_win.wait_page(Constants.URL_FEEDS_ORDER)
        assert driver.current_url == Constants.URL_FEEDS_ORDER
    @allure.feature('Проверяем открытие всплывающего окна')
    def test_click_ingredient_pop_up_modul_ingredient(self, driver):
        modal_win = BaseFunction(driver)
        modal_win.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        modal_win.click_button_ingredient()
        href = modal_win.get_button_ingredient_href()
        assert driver.current_url == href

    @allure.feature('Закрываем всплывающее окно по крестику')
    def test_click_close_ingredient_go_main_page(self, driver):
        modal_win = BaseFunction(driver)
        modal_win.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        modal_win.click_button_ingredient()
        modal_win.click_close_modul_ingredient()
        element = modal_win.get_first_ingredient()
        print(element)
        assert 'opened' not in element

    @allure.feature('При добавлении ингредиента в заказ, счетчик увеличивается')
    def test_add_ingredient_count_increases(self, driver):
        element = BaseFunction(driver)
        element.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        element.drag_and_drop_element(driver)
        count = element.get_first_ingredient_count()
        assert count == '2'

    @allure.feature('Проверяем залогиненный пользователь может создать заказ')
    def test_login_user_create_order_ok(self, login):
        create_order = BaseFunction(login)
        create_order.wait_page(Constants.URL_MAIN_PAGE)
        create_order.drag_and_drop_element(login)
        create_order.click_order_create()
        create_order.get_number_order()
        assert create_order.order_create_ok() == Constants.ORDER_CREATE_TEXT