#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
from time import sleep
from web_test.data.The_login_data import the_Login
from web_test.public.Denglu import Deng_lu
from web_test.data.search_data import Search
import re
import time,HTMLTestRunner

from web_test.public.Screen_shot import Screenshot


class Search_c(unittest.TestCase):
    u"""全视频检索"""
    driver = webdriver.Firefox()
    def setUp(self):
        dr = self.driver
        dr.get("http://t.yqboom.com")
    #
    # @unittest.skip('test_search_1')
    def test_1search_c(self):
        u"""大搜索，使用关键字搜索后查看“近7天”各来源是否显示视频数据"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['全视频检索'][0]).click()
        sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['输入文本框'][0]).send_keys("哈哈")
        sleep(5)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['搜索按钮'][0]).click()
        sleep(5)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['近7天'][0]).click()
        sleep(4)
        self.driver.implicitly_wait(30)
        doy = self.driver.find_element_by_xpath(Search['D抖音视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", doy))
        sleep(5)
        self.driver.implicitly_wait(30)
        weib = self.driver.find_element_by_xpath(Search['D微博视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", weib))
        sleep(5)
        self.driver.implicitly_wait(30)
        tt = self.driver.find_element_by_xpath(Search['D头条视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", tt))
        sleep(5)
        self.driver.implicitly_wait(30)
        kuais = self.driver.find_element_by_xpath(Search['D快手视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", kuais))
        sleep(5)
        self.driver.implicitly_wait(30)
        try:
            self.assertTrue(re.findall(r"\d+\.?\d*", doy) > ['1'], msg='抖音视频数小于1，没有数据')
            self.assertTrue(re.findall(r"\d+\.?\d*", weib) > ['1'], msg='微博视频数小于1，没有数据')
            self.assertTrue(re.findall(r"\d+\.?\d*", tt) > ['1'], msg='头条视频数小于1，没有数据')
            self.assertTrue(re.findall(r"\d+\.?\d*", kuais) > ['1'], msg='快手视频数小于1，没有数据')
        except AssertionError as e:
            # 截图保存
            # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"全部视频数小于1，没有数据")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.makeSuite(Search_c)
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    filename = "D:\\kuangjia\\report\\"+now+"_result.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'ALIEN测试报告',
            description=u'ALIEN用例执行情况：')

    runner.run(suite)
    # 关闭文件流，不关的话生成的报告是空的
    fp.close()
