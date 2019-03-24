from selenium import webdriver
import os
import unittest


browser = os.getenv('browser', 'chrome')


chrome_path = '../drivers/chromedriver'
firefox_gecko_path = '../drivers/geckodriver'


class TestDriver(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if browser == 'chrome':
            cls.driver = webdriver.Chrome(executable_path=chrome_path)
        elif browser == 'firefox':
            cls.driver = webdriver.Firefox(executable_path=firefox_gecko_path)
        # other browsers can be done in the same way

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()