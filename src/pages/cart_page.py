from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class CartPage(BasePage):
    CONTAINER = (By.ID, 'cart_contents_container')
    ITEMS = (By.CLASS_NAME, 'cart_item')
    CHECKOUT_BTN = (By.ID, 'checkout')

    def is_loaded(self):
        try:
            return self.find(*self.CONTAINER) is not None
        except Exception:
            return False

    def get_items(self):
        names = []
        try:
            items = self.finds(*self.ITEMS)
            for it in items:
                names.append(it.find_element(By.CLASS_NAME, 'inventory_item_name').text)
        except Exception:
            pass
        return names

    def remove_item(self, product_name):
        xpath = f"//div[@class='cart_item']//div[text()=\"{product_name}\"]/ancestor::div[@class='cart_item']//button[contains(text(),'Remove')]"
        try:
            btn = self.driver.find_element(By.XPATH, xpath)
            btn.click()
        except Exception:
            pass

    def go_to_checkout(self):
        self.find(*self.CHECKOUT_BTN).click()
