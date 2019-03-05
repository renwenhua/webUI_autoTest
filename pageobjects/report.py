#!usr/bin/env python
#encoding:utf-8
import unittest
from testsuites.test_fourth import Fourthtest
from testsuites.test_one import DiscuzSearch
from testsuites.test_two import Twotest
from testsuites.test_three import Threetest
import os
import HTMLTestRunner

cur_path=os.path.dirname(os.path.realpath(__file__))

report_path=os.path.join(cur_path ,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Fourthtest))
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(Twotest))
suite.addTest(unittest.makeSuite(Threetest))

if __name__=='__main__':

    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    runnet=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runnet.run(suite)

    # runnet=unittest.TextTestRunner(verbosity=2)
    # runnet .run(suite)