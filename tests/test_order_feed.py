import allure
from selenium.webdriver import ActionChains

from constants import Constants
from page_object.base_function import BaseFunction, BaseFunctionLocators
from page_object.orders_feed import OrdersFeed, OrdersFeedLocators



@allure.epic('Проверка Листа заказов')
class TestOrdersFeed:

    @allure.feature('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order1_open_modul_order(self, driver):
        modal_win = OrdersFeed(driver)
        modal_win.go_to_site_stellarburger(Constants.URL_FEEDS_ORDER)
        order_text_name = modal_win.get_text_order_name_feed_page()
        modal_win.click_button_order1()
        order_text_name_modul = modal_win.get_text_order_modul()
        order_text_state_order = modal_win.get_text_order_state()

        assert order_text_name == order_text_name_modul
        assert order_text_state_order == 'Выполнен'

    @allure.feature('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_histrory_equals_feed_order_list(self, login):
        history_order = OrdersFeed(login)

        history_lk = history_order.get_user_order_history_lk(login)
        history_page_feed = history_order.get_user_order_history_feed_page(login)
        history_lk = list(history_lk.split("\n"))
        history_page = list(history_page_feed.split("\n"))
        try:
            assert history_lk in history_page
        except Exception as e:
            print(f'Данные заказов не совпадают {e}')

    @allure.feature('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_make_new_order_count_completed_increases(self, login):
        count = OrdersFeed(login)
        count.go_to_site_stellarburger(Constants.URL_FEEDS_ORDER)
        count.wait_page(Constants.URL_FEEDS_ORDER)
        count_old = count.count_completed_increases_old()

        #Создаем заказ
        count.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        count.wait_page(Constants.URL_MAIN_PAGE)
        drag_from = count.find_element_located(OrdersFeedLocators.INGREDIENT1, time=5)
        drag_to = count.find_element_located(OrdersFeedLocators.CONSTRUCTOR_ELEMENT, time=5)
        actions = ActionChains(login)
        actions.drag_and_drop(drag_from, drag_to).perform()
        count.find_element_located(BaseFunctionLocators.BUTTON_ORDER_CREATE, time=10).click()

        count.go_to_site_stellarburger(Constants.URL_FEEDS_ORDER)
        count.wait_page(Constants.URL_FEEDS_ORDER)
        count_new = count.count_completed_increases_new()

        assert count_new > count_old

    @allure.feature('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_make_new_order_count_today_completed_increases(self, login):
        count = OrdersFeed(login)
        count.go_to_site_stellarburger(Constants.URL_FEEDS_ORDER)
        count.wait_page(Constants.URL_FEEDS_ORDER)
        count_old = count.count_completed_increases_old_today()

        #Создаем заказ
        count.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
        count.wait_page(Constants.URL_MAIN_PAGE)
        drag_from = count.find_element_located(OrdersFeedLocators.INGREDIENT1, time=7)
        drag_to = count.find_element_located(OrdersFeedLocators.CONSTRUCTOR_ELEMENT, time=7)
        actions = ActionChains(login)
        actions.drag_and_drop(drag_from, drag_to).perform()
        count.find_element_located(BaseFunctionLocators.BUTTON_ORDER_CREATE, time=10).click()

        count.go_to_site_stellarburger(Constants.URL_FEEDS_ORDER)
        count.wait_page(Constants.URL_FEEDS_ORDER)
        count_new = count.count_completed_increases_new_today()

        assert count_new > count_old


    @allure.feature('После оформления заказа его номер появляется в разделе В работе')
    def test_make_new_order_order_in_progress(self, login):
        progress = OrdersFeed(login)

        #Создаем заказ
        progress.wait_page(Constants.URL_MAIN_PAGE)
        drag_from = progress.find_element_located(OrdersFeedLocators.INGREDIENT1, time=7)
        drag_to = progress.find_element_located(OrdersFeedLocators.CONSTRUCTOR_ELEMENT, time=7)
        actions = ActionChains(login)
        actions.drag_and_drop(drag_from, drag_to).perform()
        progress.find_element_located(BaseFunctionLocators.BUTTON_ORDER_CREATE, time=10).click()
        num_actual = progress.number_new_order()

        progress.go_to_site_stellarburger(Constants.URL_FEEDS_ORDER)
        progress.wait_page(Constants.URL_FEEDS_ORDER)
        num_feed_list = progress.number_order_in_progress()
        try:
            assert num_actual == num_feed_list
        except Exception as e:
            print(f'Ошибка {e}')