from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class PersonalAccountLocators:
    # Кнопка Личный кабинет на главной странице
    BUTTON_LK = (By.XPATH, ".//a[@href='/account']")
    #Ссылка ведущая в Историю заказов авторизованного пользователя
    LINK_ORDER_HISTORY = (By.XPATH, ".//a[@href='/account/order-history']")
    #Поле ввода логин на форме авторизации
    INPUT_LOGIN_AUTH = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    #Поле ввода пароля на форме авторизации
    INPUT_PASS_AUTH = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    #Кнопка Войти на форме Авторизации
    BUTTON_AUTH = (By.XPATH,".//button[text()='Войти']")
    #Кнопка выйти из ЛК
    BUTTON_LOGOUT = (By.XPATH,".//button[contains(text(),'Выход')]")


class PersonalAccount(BasePage):
    #Кликаем на кнопку Личный кабинет
    def click_button_lk(self):
        self.find_element_located(PersonalAccountLocators.BUTTON_LK, time=3).click()

    #Переход в Историю заказов
    def click_button_order_history(self):
        self.find_element_located(PersonalAccountLocators.LINK_ORDER_HISTORY, time=3).click()

    #Выход из аккаунта
    def click_button_logout(self):
        self.find_element_located(PersonalAccountLocators.BUTTON_LOGOUT, time=3).click()