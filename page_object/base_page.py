from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site_stellarburger(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator, time=12):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

#Использовать при задержке страницы
    def wait_page(self, url):
        return WebDriverWait(self.driver, 5).until(EC.url_contains(url))
