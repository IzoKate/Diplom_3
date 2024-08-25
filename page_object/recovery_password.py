from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class RecoveryPageLocators:
    # Кнопка Личный кабинет на главной странице
    BUTTON_LK = (By.XPATH, ".//a[@href='/account']")
    #Кнопка Восстановить на форме восстановления пароля
    BUTTON_FOGOT_PASSWORD = (By.XPATH, ".//button[text()='Восстановить']")
    #Кнопка Войти на Главной странице
    BUTTON_LOGIN_MAIN_PAGE = (By.XPATH, ".//button[text()='Войти в аккаунт']")


    # Кликабельная ссылка Восстановить пароль на форме входа в аккаунт
    LINK_FORGOT_PASSWORD = (By.XPATH, ".// a[ @ href = '/forgot-password']")

    # Поле ввода E-mail на форме восстановления пароля
    INPUT_EMAIL = (By.XPATH, ".//input[@name='name']")
    # Поле ввода парол  с без подсветки
    INPUT_PASSWORD =  (By.XPATH, ".//div[contains(@class, 'status_active')]")

    #Кнопка показать\скрыть пароль
    BUTTON_ON_OFF_PASSWORD = (By.XPATH, ".//div[contains(@class, 'input')]/*[name()='svg']")

    #Подсветка поля пароль
    LIGHT_INPUT = (By.XPATH, ".//div[contains(@class, 'input')]/*[name()='svg']")

    #Локатор логотипа
    LOGO_SCOOTER = (By.XPATH,"//img[@alt='Scooter']")


class RecoveryPage(BasePage):
    #Кликаем на кнопку Личный кабинет
    def click_button_lk(self):
        self.find_element_located(RecoveryPageLocators.BUTTON_LK, time=3).click()

    #Кликаем на кнопку Войти в аккаунт
    def click_button_login_account(self):
        self.find_element_located(RecoveryPageLocators.BUTTON_LOGIN_MAIN_PAGE, time=3).click()

    #Кликаем на ссылку Восстановить пароль на странице восстановления пароля
    def click_link_forgot_password(self):
        self.find_element_located(RecoveryPageLocators.LINK_FORGOT_PASSWORD, time=3).click()

    #Кликаем на кнопку Восстановить  на странице восстановления пароля
    def click_button_forgot_password(self):
        self.find_element_located(RecoveryPageLocators.BUTTON_FOGOT_PASSWORD, time=3).click()

    #Кликаем на кнопку показать\скрыть пароль
    def click_button_on_off_password(self):
        self.find_element_located(RecoveryPageLocators.BUTTON_ON_OFF_PASSWORD, time=3).click()

    #Вводим e-mail
    def set_email(self, email):
        self.find_element_located(RecoveryPageLocators.INPUT_EMAIL, time=3).send_keys(email)

    #Ищем подсветку
    def find_input_light(self):
        self.find_element_located(RecoveryPageLocators.LIGHT_INPUT, time=4)
        return True
