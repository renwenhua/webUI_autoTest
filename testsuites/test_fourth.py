#!usr/bin/env python
#encoding:utf-8
from testsuites.base_testcase import BaseTestCase
from pageobjects.page_login import Login
from pageobjects.page_findfile import Findfile
from pageobjects.page_exit import Exit
from pageobjects.page_toupiao import Tou
from pageobjects.page_vote_on import Voteon
from pageobjects.page_vata import Vata

class Fourthtest(BaseTestCase):
    def test_threetest(self):
        #登录
        log=Login(self.driver)
        log.login("aaa","123321")
        self.assertIn("论坛", self.driver.title, "登录")
        #发起投票
        tou=Tou(self.driver)
        tou.toupiao("应该去吗？","同意","不同意","中立","wwwwwwwwwwwwwwwwwwwwww")
        self.assertIn("默认版块", self.driver.title, "登录")
        #进行投票
        vo=Voteon(self.driver)
        vo.vote_on()
        #取值
        vata=Vata(self.driver)
        vata.vata()
