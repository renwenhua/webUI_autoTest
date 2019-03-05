#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class New_plate(BasePage):
    manage_frame=(By.TAG_NAME, "iframe")
    manage_new = (By.PARTIAL_LINK_TEXT, "添加新版块")
    manage_submit=(By.CSS_SELECTOR,".fixsel .btn")
    def newplate(self):
        self.frame(*self.manage_frame)
        self.click(*self.manage_new)
        self.click(*self.manage_submit)