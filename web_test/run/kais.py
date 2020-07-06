import HTMLTestRunner
import unittest
from time import strftime, localtime, time

from web_test.Automation  import Register
from web_test.Automation.Register import The_login2

suite = unittest.TestSuite()
# 获取TestSuite的实例对象
suite.addTest(Register.The_login2("test_denglu_4"))
# 把测试用例添加到测试容器中

now = strftime("%Y-%m-%d %H_%M_%S", localtime(time()))
# 获取当前时间
filename ="D:\\kuangjia\\web_test\\report\\" +now + "test.html"
# 文件名

fp = open(filename, "wb+")
# 以二进制的方式打开文件并写入结果
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title="测试报告的标题",
    description="测试报告的详情")

runner.run(suite)

fp.close()

