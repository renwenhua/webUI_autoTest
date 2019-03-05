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
        #��¼
        # url="http://127.0.0.1/forum.php"
        home_page=Login(self.driver)
        # home_page.open_url(url)
        home_page.login("admin","123321")
        self.assertIn("��̳",self.driver.title,"��¼")
        #��鷢��
        ps=Post(self.driver)
        ps.moban()
        self.assertIn("Ĭ�ϰ��", self.driver.title, "Ĭ�ϰ��")
        ps.section("����","aaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.assertIn("�����б�", self.driver.page_source)
        ps.get_windows_img()
        # #����
        rp=Reply(self.driver)
        rp.reply("cdrhgkt3uygu5bgefrl")
        self.assertIn("Ĭ�ϰ��", self.driver.title, "����")
        # #�˳�
        et=Exit(self.driver)
        et.exit()


if __name__=='__main__':
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run()