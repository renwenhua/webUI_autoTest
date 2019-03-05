#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

#登录
class Vata(BasePage):
    name1 = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[1]")
    data1 = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[2]")
    name2 = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[3]")
    data2 = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[4]")
    name3 = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[5]")
    data3 = (By.XPATH, "//*[@class='pcht']/table/tbody/tr[6]")
    title = (By.CSS_SELECTOR, "h1")

    def vata(self):
        self.gettext(*self.name1)
        self.gettext(*self.data1)
        self.gettext(*self.name2)
        self.gettext(*self.data2)
        self.gettext(*self.name3)
        self.gettext(*self.data3)
        self.gettext(*self.title)
