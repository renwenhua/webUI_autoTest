import os
import sys
import unittest
import HTMLTestRunner
import unittest
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append("E:\\pythonWorkplace\\UITest")



test_dir='./'
suite=unittest.TestLoader().discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    runnet=unittest.TextTestRunner(verbosity=2)
    runnet .run(suite)