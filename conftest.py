import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from page_object.personal_account import PersonalAccountLocators
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

#Авторизация в ЛК
@pytest.fixture
def login(driver):
    driver.get(Constants.URL_MAIN_PAGE)
    WebDriverWait(driver, 12).until(EC.presence_of_element_located(PersonalAccountLocators.BUTTON_LK), message=f'Not found locator').click()
    WebDriverWait(driver, 12).until(EC.presence_of_element_located(PersonalAccountLocators.INPUT_LOGIN_AUTH), message=f'Not found locator').send_keys(Constants.EMAIL)
    WebDriverWait(driver, 12).until(EC.presence_of_element_located(PersonalAccountLocators.INPUT_PASS_AUTH), message=f'Not found locator').send_keys(Constants.PASSWORD)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(PersonalAccountLocators.BUTTON_AUTH), message=f'Not found locator').click()
    WebDriverWait(driver, 15).until(EC.url_contains(Constants.URL_LOGIN))
    return driver