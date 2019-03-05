from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

#模板 发帖 标题内容
class Post(BasePage):
    discuz_page_btn_section_loc=(By.CSS_SELECTOR,".fl_icn a")
    # discuz_page_post_section_loc=(By.CSS_SELECTOR,"#pgt a img")
    discuz_page_title_section_loc = (By.CSS_SELECTOR, "#subject")
    # discuz_page_frame_section_loc = (By.TAG_NAME, "iframe")
    discuz_page_contact_section_loc = (By.CSS_SELECTOR, "#fastpostmessage")
    discuz_page_fabiao_section_loc = (By.CSS_SELECTOR, "#fastpostsubmit")


    def moban(self):
        self.click(*self.discuz_page_btn_section_loc)
    def section(self,title,content):
        # self.click(*self.discuz_page_post_section_loc)
        self.sendkeys(title,*self.discuz_page_title_section_loc)
        # self.frame(*self.discuz_page_frame_section_loc)
        self.sendkeys(content,*self.discuz_page_contact_section_loc)
        self.click(*self.discuz_page_fabiao_section_loc)

