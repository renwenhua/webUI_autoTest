import logging
import os.path
import time


class Log(object):
    def __init__(self,logger):
        self.loger=logging.getLogger()
        self.loger.setLevel(logging.DEBUG)


        rq=time.strftime("%Y%m%d%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+'/logs/'
        log_name=log_path+rq+'.log'
        ch=logging.StreamHandler()
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)


        format=logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        ch.setFormatter(format)
        fh.setFormatter(format)
        self.loger.addHandler(ch)
        self.loger.addHandler(fh)
    def getlog(self):
        return self.loger