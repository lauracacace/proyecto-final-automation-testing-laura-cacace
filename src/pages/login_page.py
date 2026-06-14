from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    ERROR_MSG = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def login(self, username, password):
        self.find(*self.USERNAME).clear()
        self.find(*self.USERNAME).send_keys(username)
        self.find(*self.PASSWORD).clear()
        self.find(*self.PASSWORD).send_keys(password)
        self.find(*self.LOGIN_BTN).click()

    def get_error(self):
        try:
            return self.find(*self.ERROR_MSG).text
        except Exception:
            return ''