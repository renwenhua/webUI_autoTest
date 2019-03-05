from selenium import webdriver
import unittest
from  framework.browserengin import BrowserEngin

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        be = BrowserEngin()
        self.driver=be.open_browser()
    def tearDown(self):
        self.driver.quit()
