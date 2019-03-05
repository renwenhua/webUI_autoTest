from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
#登录
class Login(BasePage):
    discuz_page_name_login_loc=(By.NAME,"username")
    discuz_page_psw_login_loc=(By.NAME,"password")
    discuz_page_btn_login_loc=(By.CSS_SELECTOR, "button em")
    def login(self,name,psw):
        self.sendkeys(name,*self.discuz_page_name_login_loc)
        self.sendkeys(psw,*self.discuz_page_psw_login_loc)
        self.click(*self.discuz_page_btn_login_loc)


