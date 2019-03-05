#!usr/bin/env python
#encoding:utf-8
from testsuites.base_testcase import BaseTestCase
from pageobjects.page_login import Login
from pageobjects.page_findfile import Findfile
from pageobjects.page_exit import Exit


class Threetest(BaseTestCase):
    def test_threetest(self):
        # 用户登录
        login = Login(self.driver)
        login.login("aaa", "123321")
        self.assertIn("论坛", self.driver.title, "登录")
        #搜索 验证
        find=Findfile(self.driver)
        find.find("haotest")
        #退出
        exit = Exit(self.driver)
        exit.exit()
        self.assertIn("提示信息", self.driver.title, "退出")

