import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, text):
        self.driver.find_element_by_xpath(locator).send_keys(text)

    def type_and_enter(self, locator, text):
        self.driver.find_element_by_xpath(locator).send_keys(text)
        self.driver.find_element_by_xpath(locator).send_keys(Keys.ENTER)

    def get_web_page(self, address):
        self.driver.get(address)

    def press(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def wait_for_element(self, locator, timeout=60):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def is_element_visible(self, locator):
        return self.driver.find_element_by_xpath(locator).is_displayed()

    def is_element_present(self, locator):
        return self.driver.find_element_by_xpath(locator).is_displayed()
