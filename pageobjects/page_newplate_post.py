#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

#登录
class Login(BasePage):
    post_new=(By.PARTIAL_LINK_TEXT,"新版块名称")
    def post(self,name,psw):
        self.click(name,*self.post_new)



