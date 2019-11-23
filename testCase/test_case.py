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
        result = r.getRequest(url,param,method)
        real = json.loads(result)['errorCode']
        try:
            if self.assertEqual(real,int(expect)) == None:
                w.writeResult(int(id),real,"Success")
        except AssertionError as msg:
            w.writeResult(int(id),real,'Fail')




if __name__=='__main__':
    unittest.main()
