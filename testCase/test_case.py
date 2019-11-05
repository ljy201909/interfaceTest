# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.02

import unittest
import json
from ddt import ddt,data,unpack
import requests

from common.readExcel import readExcel

d = readExcel()
testda = d.assembleData()

@ddt
class MyTestCase1(unittest.TestCase):

    @data(*testda)
    @unpack
    def test1(self,id,url,method,param,expect):
        #print(id,url,method,param,expect)
        param = json.loads(param)
        if method == 'post':
            response = requests.post(url=url,data=param)
            #print(response.status_code)
        else:
            response = requests.get(url=url,params=param)
            #print(response.status_code)
        #将response的text放入result，方便断言
        # result = response.text
        # print(result)
        # print(type(result))
        # real = result.json()['errorCode']
        real = json.loads(response.text)['errorCode']
        #print(real)
        # print(type(real))
        # print(type(expect))
        try:
            if self.assertEqual(real,int(expect)) == None:
                result = 'Success'
                print('验证结果',result)
        except AssertionError as msg:
            #print(msg)
            result = 'Fail'
            print('验证结果', result)



if __name__=='__main__':
    unittest.main()
