from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.CLASS_NAME, 'inventory_details_name')
    ADD_BTN = (By.CSS_SELECTOR, 'button.btn_primary')

    def get_title(self):
        try:
            return self.find(*self.TITLE).text
        except Exception:
            return ''

    def add_to_cart(self):
        try:
            self.find(*self.ADD_BTN).click()
        except Exception:
            pass
