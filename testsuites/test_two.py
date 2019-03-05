#!usr/bin/env python
#encoding:utf-8
import unittest
from pageobjects.page_plate_management import Manage
from testsuites.base_testcase import BaseTestCase
from pageobjects.page_login import Login
from pageobjects.page_delete import Delete
from pageobjects.page_new_plate import New_plate
from pageobjects.page_exit import Exit
from pageobjects.page_post import Post
from pageobjects.page_reply import Reply
class Twotest(BaseTestCase):
    def test_twotest(self):
        #管理员登录
        login=Login(self.driver)
        login.login("admin","123321")
        self.assertIn("论坛", self.driver.title, "登录")
        #进入模板
        post=Post(self.driver)
        post.moban()
        self.assertIn("默认版块", self.driver.title, "默认版块")
        #删除帖子
        det=Delete(self.driver)
        det.delete()
        #板块管理
        man=Manage(self.driver)
        man.manage()
        self.assertIn("管理中心",self.driver.title)
        #添加新版块
        new=New_plate(self.driver)
        new.newplate()
        #管理员退出
        exit=Exit(self.driver)
        exit.exit()
        self.assertIn("提示信息", self.driver.title, "退出")
        # 用户登录
        login = Login(self.driver)
        login.login("aaa", "123321")
        self.assertIn("默认版块", self.driver.title, "登录")
        #新版块发帖
        ps = Post(self.driver)
        # ps.moban()
        ps.section("标题2", "ssssssssss")
        self.assertIn("返回列表", self.driver.page_source)
        ps.get_windows_img()
        # 回帖
        rp = Reply(self.driver)
        rp.reply("ZZZZZZZZZZZZZ")
        self.assertIn("默认版块", self.driver.title, "回帖")

