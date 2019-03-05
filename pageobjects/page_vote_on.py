#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

#登录
class Voteon(BasePage):
    one=(By.CLASS_NAME, "pslt")
    put=(By.CSS_SELECTOR,"#pollsubmit")
    def vote_on(self):
        self.click(*self.one)
        self.click(*self.put)


