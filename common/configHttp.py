# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.02

import  requests
from common import readConfig as readConfig

class ConfigHttp(object):

    #get方法
    def get(self,url,param):
        try:
            # param = eval(param)
            # print(type(param))
            respone = requests.get(url,params=eval(param))
            result = respone.text
            return result
        except Exception:
            print('request error,please check out!')
            return None

    #post方法
    def post(self,url,param):
        try:
            respone = requests.post(url,data=eval(param))
            print(type(eval(param)))
            result = respone.text
            print(result)
            return result
        except Exception:
            print('request error,please check out!')
            return None

    def getRequest(self,url,param,method):
        if str(method) == 'get':
            self.get(url,param)
        elif str(method) == "post":
            self.post(url,param)



# #---------调试信息
# c = ConfigHttp()
# url = 'https://www.wanandroid.com/user/login'
#
# param = '{"username":"lijingying","password":"123456"}'
#
# c.getRequest(url,param,'post')
