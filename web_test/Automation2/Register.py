#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import  unittest,time
from time import sleep

from data.The_login_data import the_Login
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
        text2 = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/span[1]/span").text
        self.assertEqual(text2,'数据大屏',msg='没有获取到数据大屏文本登录失败')
        sleep(5)
        if u'数据大屏' == text2:
            print('用例通过，登录成功')
        else:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"错误,账号密码输入正确但不能正常登录")
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()