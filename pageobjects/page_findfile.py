#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

#登录
class Findfile(BasePage):
    enter_file=(By.CSS_SELECTOR,"#scbar_txt")
    sousuo=(By.CSS_SELECTOR,"#scbar_btn")
    hotset_serch=(By.PARTIAL_LINK_TEXT,"haotest")
    def find(self,word):
        self.sendkeys(word,*self.enter_file)
        self.click(*self.sousuo)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.hotset_serch)
        self.driver.switch_to.window(self.driver.window_handles[2])
        assert "haotest" in self.driver.title
