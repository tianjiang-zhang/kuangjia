#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
from time import sleep
from data.The_login_data import the_Login
from public.Denglu import Deng_lu
from data.search_data import Search
import re
from public.Screen_shot import Screenshot


class Search_(unittest.TestCase):
    u"""全视频检索"""
    driver = webdriver.Firefox()
    def setUp(self):
        dr = self.driver
        dr.get("http://t.yqboom.com")
    #
    # @unittest.skip('test_search_1')
    def test_1search(self):
        u"""大搜索，使用关键字搜索后查看“24小时内”是否显示视频数据"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['全视频检索'][0]).click()
        sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['输入文本框'][0]).send_keys("哈哈")
        sleep(1)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['搜索按钮'][0]).click()
        sleep(5)
        self.driver.find_element_by_xpath(Search['24小时'][0]).click()
        sleep(4)
        string = self.driver.find_element_by_xpath(Search['全部视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", string))



        try:
            self.assertTrue(re.findall(r"\d+\.?\d*", string)>['1'],msg='全部视频数小于1，没有数据')
        except AssertionError as e:
            # 截图保存
            # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"全部视频数小于1，没有数据")

    # @unittest.skip('test_search_2')
    def test_2search(self):
        u"""大搜索，使用关键字搜索后查看“今天内”是否显示视频数据"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['全视频检索'][0]).click()
        sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['输入文本框'][0]).send_keys("哈哈")
        sleep(1)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['搜索按钮'][0]).click()
        sleep(5)
        self.driver.find_element_by_xpath(Search['今天'][0]).click()
        sleep(4)
        string = self.driver.find_element_by_xpath(Search['全部视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", string))
        try:
            self.assertTrue(re.findall(r"\d+\.?\d*", string)>['1'],msg='全部视频数小于1，没有数据')
        except AssertionError as e:
            # 截图保存
            # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"全部视频数小于1，没有数据")


    # @unittest.skip('test_search_3')
    def test_3search(self):
        u"""大搜索，使用关键字搜索后查看“7天内”是否显示视频数据"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['全视频检索'][0]).click()
        sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['输入文本框'][0]).send_keys("哈哈")
        sleep(1)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['搜索按钮'][0]).click()
        sleep(5)
        self.driver.find_element_by_xpath(Search['近7天'][0]).click()
        sleep(4)
        string = self.driver.find_element_by_xpath(Search['全部视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", string))
        try:
            self.assertTrue(re.findall(r"\d+\.?\d*", string)>['1'],msg='全部视频数小于1，没有数据')
        except AssertionError as e:
            # 截图保存
            # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"全部视频数小于1，没有数据")

    def test_4search(self):
        u"""大搜索，使用关键字搜索后查看“近30天”是否显示视频数据"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        sleep(10)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['全视频检索'][0]).click()
        sleep(3)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['输入文本框'][0]).send_keys("哈哈")
        sleep(1)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(Search['搜索按钮'][0]).click()
        sleep(5)
        self.driver.find_element_by_xpath(Search['近30天'][0]).click()
        sleep(4)
        string = self.driver.find_element_by_xpath(Search['全部视频数'][0]).text
        print(re.findall(r"\d+\.?\d*", string))
        try:
            self.assertTrue(re.findall(r"\d+\.?\d*", string)>['1'],msg='全部视频数小于1，没有数据')
        except AssertionError as e:
            # 截图保存
            # 新创建路径“.”表示当前整个.py文件的路径所在的位置，“\\”路径分割符，其中的一个是“\”表示转义字符
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"全部视频数小于1，没有数据")

    def tsetDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
