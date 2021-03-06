from configparser import ConfigParser
from selenium import webdriver
from framework.logger import *


loger=Log(logger="Login").getlog()
class BrowserEngin(object):
    dir=os.path.dirname(os.path.abspath("."))#相对路径获取方法
    chrome_driver_path=dir+'/tools/chromedriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    firefox_driver_path=dir+'/tools/geckodriver.exe'

    #read the browser type from config.ini file,return the driver
    #从config.ini文件读取浏览器类型，返回驱动程序
    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path)

        browser=config.get("browserType","browserName")
        loger.info("你选择了%s游览器."%browser)#you had selectt %s browser
        url=config.get("testServer","URL")
        loger.info("测试URL是:%s" %url)  # the test server url is

        if browser =="Firefox":
            driver=webdriver.Firefox(self.firefox_driver_path)#启动Firefox
            loger.info("启动火狐游览器")
        elif browser =="Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            loger.info("启动谷歌游览器")
        elif browser =="IE":
            driver = webdriver.Ie(self.ie_driver_path)
            loger.info("启动IE游览器")

        driver.get(url)
        loger.info("打开：%s"%url)
        driver.maximize_window()
        loger.info("窗口最大化")
        driver.implicitly_wait(10)
        loger.info("等待10秒")
        return driver

    def quit_browser(self):
        loger.info("关闭游览器")
        self.driver.quit()