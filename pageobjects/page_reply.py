from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class Reply(BasePage):
    butten_reply=(By.CSS_SELECTOR,"#post_reply img")
    butten_reply_content = (By.CSS_SELECTOR, ".p_c .tedt .area textarea")
    butten_reply_submit = (By.CSS_SELECTOR, "#moreconf #postsubmit span")
    def reply(self,text):
        self.click(*self.butten_reply)
        self.sendkeys(text,*self.butten_reply_content)
        self.click(*self.butten_reply_submit)
