#!usr/bin/env python
#encoding:gbk
import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.page_login import Login
from pageobjects.page_post import Post
from pageobjects.page_reply import Reply
from pageobjects.page_exit import Exit

class DiscuzSearch(BaseTestCase):
    def test_one(self):
        #登录
        # url="http://127.0.0.1/forum.php"
        home_page=Login(self.driver)
        # home_page.open_url(url)
        home_page.login("admin","123321")
        self.assertIn("论坛",self.driver.title,"登录")
        #板块发帖
        ps=Post(self.driver)
        ps.moban()
        self.assertIn("默认版块", self.driver.title, "默认版块")
        ps.section("标题","aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertIn("返回列表", self.driver.page_source)
        ps.get_windows_img()
        # #回帖
        rp=Reply(self.driver)
        rp.reply("cdrhgkt3uygu5bgefrl")
        self.assertIn("默认版块", self.driver.title, "回帖")
        # #退出
        et=Exit(self.driver)
        et.exit()


if __name__=='__main__':
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run()