from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage


def test_remove_from_cart(driver, base_url):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login('standard_user', 'secret_sauce')
    inv = InventoryPage(driver)
    product = 'Sauce Labs Backpack'
    inv.add_to_cart(product)
    inv.go_to_cart()
    cart = CartPage(driver)
    assert product in cart.get_items()
    cart.remove_item(product)
    # reload cart items
    items = cart.get_items()
    assert product not in items
