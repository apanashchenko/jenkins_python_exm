from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_search(driver):
        wait_until(driver, 30, By.NAME, 'q').is_displayed(), 'Search field not show!'
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('Jenkins' + Keys.RETURN)
        assert "No results found." not in driver.page_source


def wait_until(driver, timeout, by, locator):
    element_visible = EC.visibility_of_element_located((by, locator))
    return WebDriverWait(driver, timeout).until(element_visible)
