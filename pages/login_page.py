import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")  # тут осуществляется поиск поля логин и т.д
    PASSWORD_FIELD = ("xpath", "//input[@name='username'")
    SUBMIT_BUTTON = ("xpath", "//input[@name='submit'")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(ec.element_to_be_clickable(self.USERNAME_FIELD)).send_key(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(ec.element_to_be_clickable(self.PASSWORD_FIELD)).send_key(password)

    @allure.step("Click submit button")
    def enter_submit_button(self):
        self.wait.until(ec.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
