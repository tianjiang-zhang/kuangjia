#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
from time import sleep
from web_test.data.The_login_data import the_Login
from web_test.public.Denglu import Deng_lu
from web_test.data.search_data import Search
import re
from web_test.public.Screen_shot import Screenshot
from selenium.webdriver import ActionChains

class Xearch_d(unittest.TestCase):
    u"""舆情监测"""
    driver = webdriver.Firefox()
    def setUp(self):
        dr = self.driver
        dr.get("http://t.yqboom.com")
    #
    # @unittest.skip('test_search_1')
    def test_4search(self):
        u"""小搜索，使用关键字搜索后查看：时间范围“近30天内”是否显示视频数据"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(10)
        self.driver.implicitly_wait(30)
        # 鼠标悬浮操作，鼠标悬浮到“舆情监测”
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/span[2]/span/span')).perform()
        time.sleep(2)
        # 鼠标悬浮操作，鼠标悬浮到“自建方案”
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/span[2]/ul/li[2]')).perform()
        # 点击元素”哈哈“
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/span[2]/ul/li[2]/ul/div[1]/li/div/span[3]').click()
        # 获取到“抖音视频数”并截取数字
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['x近30天'][0]).click()
        self.driver.implicitly_wait(30)
        doy = self.driver.find_element_by_xpath(Search['x抖音视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", doy))
        sleep(5)
        self.driver.implicitly_wait(30)
        weib = self.driver.find_element_by_xpath(Search['x微博视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", weib))
        sleep(5)
        self.driver.implicitly_wait(30)
        tt = self.driver.find_element_by_xpath(Search['x头条视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", tt))
        sleep(5)
        self.driver.implicitly_wait(30)
        kuais = self.driver.find_element_by_xpath(Search['x快手视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", kuais))
        sleep(5)
        self.driver.implicitly_wait(30)
        try:
            self.assertTrue(re.findall(r"\d+\.?\d*", doy)>['1'],msg='抖音视频数小于1，没有数据')
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

if __name__ == "__main__":
    unittest.main()
