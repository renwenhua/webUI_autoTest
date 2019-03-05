#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class Manage(BasePage):
    manage_zhongxin = (By.PARTIAL_LINK_TEXT, "管理中心")
    manage_psw=(By.NAME,"admin_password")
    manage_log=(By.CSS_SELECTOR,".loginnofloat .btn")
    manage_luntan = (By.PARTIAL_LINK_TEXT, "论坛")

    def manage(self):
        self.click(*self.manage_zhongxin)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sendkeys("123321",*self.manage_psw)
        self.click(*self.manage_log)
        self.click(*self.manage_luntan)
