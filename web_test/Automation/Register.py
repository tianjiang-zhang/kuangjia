#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import  unittest,time
from time import sleep

from selenium.webdriver.common.by import By

from web_test.data.The_login_data import the_Login
class The_login2(unittest.TestCase):
    u"""登录"""
    driver = webdriver.Firefox()

    def setUp(self):
        dr = self.driver
        dr.get("http://t.yqboom.com")
    def test_denglu_4(self):
        u"""使用账号密码登录查看能否正常登录"""
        dr = self.driver
        dr.find_element_by_xpath(the_Login['登录试用'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号登录'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号名'][0]).send_keys('test')
        sleep(1)
        dr.find_element_by_xpath(the_Login['密码'][0]).send_keys('123456')
        sleep(1)
        dr.find_element_by_xpath(the_Login['提交'][0]).click()
        sleep(5)

        wc=dr.find_element_by_class_name("all_video_retrieval_search_box_search_button").text
        print(wc)

        self.assertEqual('搜索',wc,msg='没有获取到"搜索"文本登录失败')

        sleep(5)
        try:
            self.assertEqual(wc,'搜索')

        except AssertionError as e:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"错误,账号密码输入正确但不能正常登录")
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()