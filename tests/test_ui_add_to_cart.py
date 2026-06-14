from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage


def test_add_to_cart(driver, base_url):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login('standard_user', 'secret_sauce')
    inv = InventoryPage(driver)
    assert inv.is_loaded()
    product = 'Sauce Labs Backpack'
    inv.add_to_cart(product)
    inv.go_to_cart()
    cart = CartPage(driver)
    assert cart.is_loaded()
    items = cart.get_items()
    assert product in items
