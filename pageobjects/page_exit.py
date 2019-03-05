#!usr/bin/env python
#encoding:utf-8

from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import sys
class Exit(BasePage):
    button_exit=(By.PARTIAL_LINK_TEXT,"退出")
    def exit(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.click(*self.button_exit)