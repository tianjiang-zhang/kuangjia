#!/usr/bin/python
# -*- coding: utf-8 -*-

import HTMLTestReportCN
import unittest
import os,time
import HTMLTestReportCN
import unittest
import os,time
import HTMLTestRunner



listaa = "D:\\kuangjia\\testcase"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa, pattern='test_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="D:\\kuangjia\\report\\"+now+"_result.html"
fp=open(filename,'wb+')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'舆情系统测试报告',
    description=u'用例执行情况：')

runner.run(createsuite1())
fp.close()
