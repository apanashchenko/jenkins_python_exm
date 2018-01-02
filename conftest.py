import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.yield_fixture(scope='session')
def url():
    return 'https://www.google.com'


@pytest.yield_fixture(scope='session', name='driver')
def driver_factory(url):
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    _driver.get(url)
    yield _driver
    _driver.quit()
