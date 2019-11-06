# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.02

import unittest
import json
from ddt import ddt,data,unpack
import requests

from common.readExcel import readExcel
from common.writeExcel import writeExcel
from common.configHttp import ConfigHttp

d = readExcel()
testda = d.assembleData()
w = writeExcel()
r = ConfigHttp()

@ddt
class MyTestCase1(unittest.TestCase):

    @data(*testda)
    @unpack
    def test1(self,id,url,method,param,expect):
        #print(id,url,method,param,expect)
        # param = json.loads(param)
        result = r.getRequest(url,param,method)
        # print(result)
        # if method == 'post':
        #     response = requests.post(url=url,data=param)
        #     #print(response.status_code)
        # else:
        #     response = requests.get(url=url,params=param)
        #     #print(response.status_code)
        #将response的text放入result，方便断言
        # result = response.text
        # print(result)
        # print(type(result))
        # real = result.json()['errorCode']
        real = json.loads(result)['errorCode']
        #print(real)
        # print(type(real))
        # print(type(expect))
        try:
            if self.assertEqual(real,int(expect)) == None:
                # result = 'Success'
                #print('验证结果',result)
                w.writeResult(int(id),real,"Success")
        except AssertionError as msg:
            #print(msg)
            # result = 'Fail'
            #print('验证结果', result)
            w.writeResult(int(id),real,'Fail')




if __name__=='__main__':
    unittest.main()
