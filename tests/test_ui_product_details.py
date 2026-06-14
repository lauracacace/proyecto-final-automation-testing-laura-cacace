from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.product_page import ProductPage


def test_product_details_navigation(driver, base_url):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login('standard_user', 'secret_sauce')
    inv = InventoryPage(driver)
    product = 'Sauce Labs Backpack'
    inv.open_product(product)
    prod = ProductPage(driver)
    title = prod.get_title()
    assert product == title
