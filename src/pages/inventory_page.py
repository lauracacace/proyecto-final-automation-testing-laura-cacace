from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCTS_CONTAINER = (By.ID, 'inventory_container')
    TITLE = (By.CLASS_NAME, 'title')
    CART_LINK = (By.ID, 'shopping_cart_container')
    ITEM = (By.CLASS_NAME, 'inventory_item')

    def is_loaded(self):
        try:
            return self.find(*self.PRODUCTS_CONTAINER) is not None
        except Exception:
            return False

    def get_title(self):
        try:
            return self.find(*self.TITLE).text
        except Exception:
            return ''

    def add_to_cart(self, product_name):
        # locate product by name and click its add-to-cart button
        xpath = f"//div[@class='inventory_item']//div[text()=\"{product_name}\"]/ancestor::div[@class='inventory_item']//button[contains(text(),'Add to cart')]"
        btn = self.driver.find_element(By.XPATH, xpath)
        btn.click()

    def open_product(self, product_name):
        xpath = f"//div[@class='inventory_item']//div[text()=\"{product_name}\"]"
        elem = self.driver.find_element(By.XPATH, xpath)
        elem.click()

    def go_to_cart(self):
        self.find(*self.CART_LINK).click()

    def get_products(self):
        items = self.finds(*self.ITEM)
        names = []
        for it in items:
            try:
                names.append(it.find_element(By.CLASS_NAME, 'inventory_item_name').text)
            except Exception:
                continue
        return names