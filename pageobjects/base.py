from selenium.webdriver.support.wait import WebDriverWait
import time
import os.path
from selenium.webdriver.support import expected_conditions as EC
import unittest
from framework.logger import *

loger=Log(logger="Login").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        loger.info("back")
    def forward(self):
        self.driver.forward()
        loger.info("forward")
    def open_url(self,url):
        self.driver.get(url)
        loger.info("open_url")
    def quit_browser(self):
        self.driver.quit()
        loger.info("quit_browser")
    def close(self):
        try:
            self.driver.close()
            loger.info("close this window")
        except Exception as e:
            loger.error("filed to close this window")
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(loc))
            return self.driver.find_element(*loc)
        except:
            loger.error("%s page not found element%s元素"% (self,loc))
    def gettext(self,*loc):
        el=self.find_element(*loc)
        print(el.text)
    def sendkeys(self,text,*loc):
        try:
            el = self.find_element(*loc)
            el.clear()
            el.send_keys(text)
            loger.info("send_key"+text)
        except:
            loger.error("not send_keys")
    def clear(self,*loc):
        try:
            el=self.find_element(*loc)
            el.clear()
            loger.info("clear")
        except:
            loger.error("not clear")
    def frame(self,*loc):
        el=self.find_element(*loc)
        self.driver.switch_to.frame(el)
    def click(self,*loc):
        try:
            el = self.find_element(*loc)
            el.click()
            loger.info("click")
        except:
            loger.error("not click")
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime("%Y%m%d%M", time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            loger.info("get_windows_img")
        except:
            self.get_windows_img()
            loger.error("not get_windows_img")