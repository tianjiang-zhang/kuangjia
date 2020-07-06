#!/usr/bin/python
# -*- coding: utf-8 -*-

import HTMLTestReportCN
import unittest
import os,time
import HTMLTestReportCN
import unittest
import os,time



test_Automation = "D:\\kuangjia\\Automation"
def crea_tesuite2():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(test_Automation, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="D:\\kuangjia\\report\\"+now+"_result.html"
fp=open(filename,'wb')

runner=HTMLTestReportCN.HTMLTestRunner(
    stream=fp,
    title=u'舆情系统自动化测试报告',
    description=u'用例执行情况：')

runner.run(crea_tesuite2())
fp.close()
