from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST = (By.ID, 'first-name')
    LAST = (By.ID, 'last-name')
    POSTAL = (By.ID, 'postal-code')
    CONTINUE = (By.ID, 'continue')
    FINISH = (By.ID, 'finish')
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')

    def fill_info(self, first, last, postal):
        self.find(*self.FIRST).send_keys(first)
        self.find(*self.LAST).send_keys(last)
        self.find(*self.POSTAL).send_keys(postal)

    def continue_checkout(self):
        self.find(*self.CONTINUE).click()

    def finish(self):
        self.find(*self.FINISH).click()

    def get_complete_message(self):
        try:
            return self.find(*self.COMPLETE_HEADER).text
        except Exception:
            return ''
