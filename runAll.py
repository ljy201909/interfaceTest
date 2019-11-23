# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.10

import unittest
import time
import os
import HTMLTestRunner
from common.configEmail import ConfigEmail


def run_case(dir = 'testCase'):
    #按照指定目录加载目标用例
    case_dir = os.getcwd() + "\\" + dir

    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test_case*.py',top_level_dir=None)
    return discover

def clear_report():
    nowPath = os.path.dirname(__file__)
    print('nowpath', nowPath)
    reportPath = nowPath + "/" + "report"
    fileList = os.listdir(reportPath)
    # 如果该目录下的文件超过5个，则开始清理
    if len(fileList) > 5:
        for i in fileList:
            file = reportPath + "/" + i
            os.remove(file)

    fileNewList = os.listdir(reportPath)
    print(fileNewList)




if __name__ == '__main__':

    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.getcwd() + "\\report\\" + current_time + '.html' #生成测试报告的路径
    print(report_path)
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告',
        description=u'xx公司接口',
        verbosity=2
    )
    runner.run(run_case())
    fp.close()