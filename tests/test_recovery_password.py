import allure

from constants import Constants
from page_object.recovery_password import RecoveryPage, RecoveryPageLocators


@allure.epic('Проверка Восстановления пароля')
class TestOrderPage:
   @allure.feature('Проверяем что при клике по ссылке Восстановить пароль осуществляется переход на страницу восстановления - через кнопку ЛК')
   def test_click_button_lk_go_to_page_forgot_password(self, driver):
      rec_pass = RecoveryPage(driver)
      rec_pass.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
      rec_pass.click_button_lk()
      rec_pass.click_link_forgot_password()

      assert driver.current_url == Constants.URL_FOGOT_PASSWORD

   @allure.feature('Проверяем что при клике по ссылке Восстановить пароль осуществляется переход на страницу восстановления - через кнопку Войти в аккаунт')
   def test_click_button_login_go_to_page_forgot_password(self, driver):
      rec_pass = RecoveryPage(driver)
      rec_pass.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
      rec_pass.click_button_login_account()
      rec_pass.click_link_forgot_password()

      assert driver.current_url == Constants.URL_FOGOT_PASSWORD

   @allure.feature('Проверяем, что при вводе почты и клике по кнопку восстановить переходим на форму восстановления пароля')
   def test_click_button_restore_go_to_page_reset_password(self, driver):
      rec_pass = RecoveryPage(driver)
      rec_pass.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
      rec_pass.click_button_login_account()
      rec_pass.click_link_forgot_password()
      rec_pass.set_email(Constants.FOGOT_LOGIN)
      rec_pass.click_button_forgot_password()
      rec_pass.wait_page(Constants.URL_RESET_PASSWORD)

      assert driver.current_url == Constants.URL_RESET_PASSWORD

   @allure.feature('Проверяем, что при клике на показать\скрыть пароль появляется подсветка')
   def test_click_button_on_off_password_input_light(self, driver):
      rec_pass = RecoveryPage(driver)
      rec_pass.go_to_site_stellarburger(Constants.URL_MAIN_PAGE)
      rec_pass.click_button_login_account()
      rec_pass.click_link_forgot_password()
      rec_pass.set_email(Constants.FOGOT_LOGIN)
      rec_pass.click_button_forgot_password()
      rec_pass.wait_page(Constants.URL_RESET_PASSWORD)
      rec_pass.click_button_on_off_password()
      rec_pass.find_element_located(RecoveryPageLocators.LIGHT_INPUT)
