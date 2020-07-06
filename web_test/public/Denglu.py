#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest,time
from time import sleep
from web_test.data.The_login_data import the_Login

class Deng_lu():
    u"""登录"""
    def __init__(self,driver):
        self.driver = driver
    def denglu(self):
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
