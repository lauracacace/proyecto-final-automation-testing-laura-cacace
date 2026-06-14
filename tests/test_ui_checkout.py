from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage


def test_checkout_flow(driver, base_url):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login('standard_user', 'secret_sauce')
    inv = InventoryPage(driver)
    product = 'Sauce Labs Backpack'
    inv.add_to_cart(product)
    inv.go_to_cart()
    cart = CartPage(driver)
    cart.go_to_checkout()
    chk = CheckoutPage(driver)
    chk.fill_info('Juan', 'Perez', '12345')
    chk.continue_checkout()
    chk.finish()
    msg = chk.get_complete_message()
    assert 'THANK YOU' in msg.upper()
