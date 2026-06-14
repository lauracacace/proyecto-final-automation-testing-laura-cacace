import os
import pytest

from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.utils.csv_reader import read_csv


HERE = os.path.dirname(__file__)
DATA_FILE = os.path.normpath(os.path.join(HERE, '..', 'data', 'users.csv'))
USERS = read_csv(DATA_FILE)


@pytest.mark.ui
@pytest.mark.parametrize('user', USERS)
def test_login(driver, base_url, user):
    lp = LoginPage(driver)
    lp.open(base_url)
    lp.login(user['username'], user['password'])
    if user.get('expected', '').lower() == 'success':
        inv = InventoryPage(driver)
        assert inv.is_loaded(), 'Inventory not loaded after valid login'
    else:
        err = lp.get_error()
        assert err, 'Expected error message for invalid login'