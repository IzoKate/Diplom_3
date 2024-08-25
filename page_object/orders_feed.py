import time


from selenium.webdriver.common.by import By

from constants import Constants
from page_object.base_function import BaseFunction
from page_object.base_page import BasePage


class OrdersFeedLocators:

    #Кнопка Лента заказов
    BUTTON_ORDERS_FEED = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]")
    # Кнопка Личный кабинет на главной странице
    BUTTON_LK = (By.XPATH, ".//a[@href='/account']")
    #Ссылка ведущая в Историю заказов авторизованного пользователя
    LINK_ORDER_HISTORY = (By.XPATH, ".//a[@href='/account/order-history']")
    #Первый ингредиент
    ORDER1 = (By.XPATH, './/ul[contains(@class, "OrderFeed_list")]/li[1]')
    TEXT_ORDER1 = (By.XPATH, './/ul[contains(@class, "OrderFeed_list")]/li[1]/a/h2')

    #Окно заказа
    ORDER_MODUL_TEXT = (By.XPATH, './/div[contains(@class,"Modal_orderBox")]/h2')
    ORDER_STATE = (By.XPATH, './/div[contains(@class,"Modal_orderBox")]/p[2]')

    #Список заказов из ЛК
    ORDER_FEED_LK= (By.XPATH, './/ul[contains(@class,"OrderHistory_profileList")]')

    #Список заказов из раздела Лента заказов
    ORDER_FEED = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]')

    #Счетчик выполненных заказов
    COUNT_ORDER_COMPLETED = (By.XPATH, ".//p[text()= 'Выполнено за все время:']/following-sibling::p")
    COUNT_ORDER_TODAY_COMPLETED= (By.XPATH, ".//p[text()= 'Выполнено за сегодня:']/following-sibling::p")
    #Первый ингредиент
    INGREDIENT1 = (By.XPATH, ".//div/ul[1]/a[1]")
    #Область заказа
    CONSTRUCTOR_ELEMENT = (By.XPATH, ".//div[contains(@class, 'constructor-element')]")
    TEXT_ORDER = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")

    #Номер заказа  в окне оформления закааза
    NUM_ORDER = (By.XPATH, ".//p[text()='идентификатор заказа']/preceding-sibling::h2")

    #Заказы в работе
    ORDER_IN_PROGRESS = (By.XPATH, ".//p[text()='В работе:']/following-sibling::ul[2]/li[1]")

class OrdersFeed(BasePage):

    #Кликаем на заказ
    def click_button_order1(self):
        self.find_element_located(OrdersFeedLocators.ORDER1, time=3).click()

    # Получаем текст наименования заказа
    def get_text_order_name_feed_page(self):
        text = self.find_element_located(OrdersFeedLocators.TEXT_ORDER1, time=3).text
        return text

    # Получаем текст наименования заказа в открытом заказе
    def get_text_order_modul(self):
        text = self.find_element_located(OrdersFeedLocators.ORDER_MODUL_TEXT, time=3).text
        return text

    # Получаем текст статусы заказа
    def get_text_order_state(self):
        text = self.find_element_located(OrdersFeedLocators.ORDER_STATE, time=3).text
        return text

    # Вытаскиваем историю заказа пользователя из ЛК
    def get_user_order_history_lk(self, login):
        self.find_element_located(OrdersFeedLocators.BUTTON_LK).click()
        self.wait_page(Constants.URL_PERSONAL_ACCOUNT)
        self.find_element_located(OrdersFeedLocators.LINK_ORDER_HISTORY).click()
        self.wait_page(Constants.URL_ORDER_HISTORY)
        user_order_history = self.find_element_located(OrdersFeedLocators.ORDER_FEED_LK, time=3).text
        return user_order_history

    # Вытаскиваем историю заказа пользователя из раздела Лента заказов
    def get_user_order_history_feed_page(self, login):
        history_order = BaseFunction(login)
        history_order.click_button_orders_feed()
        user_order_history = self.find_element_located(OrdersFeedLocators.ORDER_FEED, time=3).text
        return user_order_history

    # Выполнено за все время старые данные
    def count_completed_increases_old(self):
        count_old = self.find_element_located(OrdersFeedLocators.COUNT_ORDER_COMPLETED, time=7).text
        return count_old

    # Выполнено за сегодня старые данные
    def count_completed_increases_old_today(self):
        time.sleep(2)
        count_old = self.find_element_located(OrdersFeedLocators.COUNT_ORDER_TODAY_COMPLETED, time=3).text
        return count_old

    # Выполнено за все время  после создания нового заказа
    def count_completed_increases_new(self):
        time.sleep(2)
        count_new = self.find_element_located(OrdersFeedLocators.COUNT_ORDER_COMPLETED, time=3).text
        return count_new

    # Выполнено за сегодня  после создания нового заказа
    def count_completed_increases_new_today(self):
        time.sleep(2)
        count_new = self.find_element_located(OrdersFeedLocators.COUNT_ORDER_TODAY_COMPLETED, time=3).text
        return count_new

    # Запомнить номер созданного заказа
    def number_new_order(self):
        time.sleep(2)
        num = self.find_element_located(OrdersFeedLocators.NUM_ORDER, time=5).text
        return num

    # Запомнить номер на странице заказов в работе
    def number_order_in_progress(self):
        num = self.find_element_located(OrdersFeedLocators.ORDER_IN_PROGRESS, time=2).text
        return num



