from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from conftest import driver
from constants import Constants
from page_object.base_page import BasePage


class BaseFunctionLocators:
    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[contains(text(),'Конструктор')]")
    #Кнопка Лента заказов
    BUTTON_ORDERS_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
    #Первый ингредиент
    INGREDIENT1 = (By.XPATH, ".//div/ul[1]/a[1]")
    #Счетчик первого ингредиента
    INGREDIENT1_COUNT = (By.XPATH, ".//div/ul[1]/a[1]/div/p[contains(@class, 'count')]")
    #Детали ингредиента
    DETAIL_INGREDIENT = (By.XPATH, ".//div/h2[text() = 'Детали ингредиента']")
    #Открытое окно ингредиента
    DETAIL_INGREDIENT_MODAL = (By.XPATH, ".//section[1][contains(@class, 'modal')]")
    #Кнопка закрыть окно
    BUTTON_CLOSE = (By.XPATH, ".//section[contains(@class, 'modal_opened')]/div/button[contains(@class, 'close')]")
    #Область заказа
    CONSTRUCTOR_ELEMENT = (By.XPATH, ".//div[contains(@class, 'constructor-element')]")
    # Кнопка Оформить заказ
    BUTTON_ORDER_CREATE = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")
    #Открытое окно созданного заказа
    DETAIL_ORDER_MODAL = (By.XPATH, ".//section[contains(@class, 'modal_opened')]/div/div/h2")
    #Заказ создан
    TEXT_ORDER = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")



class BaseFunction(BasePage):

    #Переход по кнопке Конструктор
    def click_button_constructor(self):
        self.find_element_located(BaseFunctionLocators.BUTTON_CONSTRUCTOR, time=3).click()

    #Переход по кнопке Лента заказов
    def click_button_orders_feed(self):
        self.find_element_located(BaseFunctionLocators.BUTTON_ORDERS_FEED, time=5).click()

    #Кликаем на ингредиент
    def click_button_ingredient(self):
        self.find_element_located(BaseFunctionLocators.INGREDIENT1, time=3).click()

    # Получаем id ингредиента
    def get_button_ingredient_href(self):
        href = self.find_element_located(BaseFunctionLocators.INGREDIENT1, time=3).get_attribute('href')
        return href

    #Кликаем на закрытие окна
    def click_close_modul_ingredient(self):
        self.find_element_located(BaseFunctionLocators.BUTTON_CLOSE, time=3).click()

    #Получаем атрибут class у первого ингредиента
    def get_first_ingredient(self):
        element = self.find_element_located(BaseFunctionLocators.DETAIL_INGREDIENT_MODAL, time=3).get_attribute('class')
        return element

    #Добавляем булку в заказ
    def add_ingredient_to_order(self):
        element = self.find_element_located(BaseFunctionLocators.INGREDIENT1_COUNT, time=3).text
        return element

    #Получаем значение счетчика
    def get_first_ingredient_count(self):
        element = self.find_element_located(BaseFunctionLocators.INGREDIENT1_COUNT, time=3).text
        return element

    #Получаем эелемент откуда нужно переместить элемент
    def drag_and_drop_element(self, driver):
        drag_from = self.find_element_located(BaseFunctionLocators.INGREDIENT1, time=3)
        drag_to = self.find_element_located(BaseFunctionLocators.CONSTRUCTOR_ELEMENT, time=3)
        actions = ActionChains(driver)
        actions.drag_and_drop(drag_from, drag_to).perform()

    #Кликаем на Оформить заказ
    def click_order_create(self):
        self.find_element_located(BaseFunctionLocators.BUTTON_ORDER_CREATE, time=3).click()

    #Получаем порядковый номер заказа
    def get_number_order(self):
        order_num = self.find_element_located(BaseFunctionLocators.DETAIL_ORDER_MODAL, time=3).text
        return order_num

    #заказ начали готовить
    def order_create_ok(self):
        text = self.find_element_located(BaseFunctionLocators.TEXT_ORDER, time=3).text
        return text





