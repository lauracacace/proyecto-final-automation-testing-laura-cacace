import os
import pytest
import logging
import datetime
from pytest_html import extras

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def _init_logging():
    logs_dir = os.path.join(os.getcwd(), 'reports', 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    log_path = os.path.join(logs_dir, 'execution.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )


@pytest.fixture(scope='session')
def base_url():
    return "https://www.saucedemo.com/"


@pytest.fixture(scope='session')
def driver(request):
    _init_logging()
    headless = os.getenv('HEADLESS', 'False').lower() in ('1', 'true', 'yes')
    options = Options()
    if headless:
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver') if 'driver' in item.funcargs else None
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), 'reports', 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{item.name}_{timestamp}.png"
            path = os.path.join(screenshots_dir, filename)
            try:
                driver.save_screenshot(path)
                logging.info(f"Saved screenshot: {path}")
                if hasattr(rep, 'extra'):
                    rep.extra.append(extras.image(path))
            except Exception as e:
                logging.exception('Failed to save screenshot')