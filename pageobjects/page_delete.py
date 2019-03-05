#!usr/bin/env python
#encoding:utf-8
from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class Delete(BasePage):
    gou_delete=(By.CSS_SELECTOR,"#threadlisttableid tbody:last-of-type .o")
    button_del = (By.PARTIAL_LINK_TEXT, "删除")
    gou_sure=(By.CSS_SELECTOR,"table #moderateform #modsubmit")
    def delete(self):
        self.click(*self.gou_delete)
        self.click(*self.button_del)
        self.click(*self.gou_sure)