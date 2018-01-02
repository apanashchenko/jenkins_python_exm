import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.yield_fixture(scope='session')
def url():
    return 'https://www.google.com'


@pytest.yield_fixture(scope='session', name='driver')
def driver_factory(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    # _driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    # _driver = webdriver.Chrome('/home/ubuntu/app/chromedriver', chrome_options=chrome_options)
    _driver = webdriver.Chrome()
    _driver.get(url)
    yield _driver
    _driver.quit()