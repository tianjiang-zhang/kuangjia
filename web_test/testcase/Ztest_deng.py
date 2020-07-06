#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
from time import sleep


from web_test.data.The_login_data import the_Login

class The_login2(unittest.TestCase):
    u"""登录"""
    driver = webdriver.Firefox()

    def setUp(self):
        dr= self.driver
        dr.get("http://t.yqboom.com")

    def test_den2(self):
        u"""账号错误查看能否正常登录"""
        sleep(5)
        dr = self.driver
        dr.get("http://t.yqboom.com")
        dr.find_element_by_xpath(the_Login['登录试用'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号登录'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号名'][0]).send_keys('test11')
        sleep(1)
        dr.find_element_by_xpath(the_Login['密码'][0]).send_keys('123456')
        sleep(1)
        dr.find_element_by_xpath(the_Login['提交'][0]).click()
        sleep(5)
        wenb = dr.find_element_by_xpath('/html/body/div/div/div[1]/p/img').is_displayed()
        try:
            self.assertTrue(wenb,)
            print('用例2通过')
        except AssertionError as e:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"错误,账号输入错误可以正常登录")
        sleep(5)

    # def tearDown(self):
    #     # self.driver.quit()


if __name__ == "__main__":
    unittest.main()
