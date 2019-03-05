#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

#模板 发帖 标题内容
class Tou(BasePage):
    toupiao_moban=(By.CSS_SELECTOR,".fl_icn a")
    toupiao_fatie = (By.CSS_SELECTOR, "#pgt a img")
    toupiao_do = (By.PARTIAL_LINK_TEXT,"发起投票")
    title=(By.CSS_SELECTOR,"#subject")
    one=(By.XPATH,"//div[@id='pollm_c_1']/p[1]/input")
    two= (By.XPATH,"//div[@id='pollm_c_1']/p[2]/input")
    three= (By.XPATH,"//div[@id='pollm_c_1']/p[3]/input")
    btn=(By.NAME,"topicsubmit")
    def toupiao(self,title,a,b,c,con):
        self.click(*self.toupiao_moban)
        self.click(*self.toupiao_fatie)
        self.click(*self.toupiao_do)
        self.sendkeys(title,*self.title)
        self.sendkeys(a,*self.one)
        self.sendkeys(b,*self.two)
        self.sendkeys(c,*self.three)
        self.click(*self.btn)