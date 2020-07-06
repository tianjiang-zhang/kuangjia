from selenium import webdriver
import unittest,time
from time import sleep

driver = webdriver.Firefox()
dr = driver
dr.get('https://uatkolbuyingautomation.lorealchina.com/')
dr.find_element_by_xpath('//*[@id="email"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="email"]').send_keys('admin@tarsocial.com')
dr.find_element_by_xpath('//*[@id="password"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="password"]').send_keys('*!Wz%5fO#JdX2&dX')
sleep(2)
dr.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[4]/div/div/span/button').click()
sleep(10)
dr.find_element_by_xpath('//*[@id="app"]/div/div/section/section/main/div/div[1]/button').click()
sleep(5)
dr.find_element_by_xpath('//*[@id="email"]').send_keys('828542515@qq.com')
sleep(5)
dr.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
sleep(5)
dr.find_element_by_xpath('//*[@id="name"]').send_keys('test1')
sleep(5)
dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div[2]/div/span/div[1]/div/div/div').click()
sleep(5)
dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div[2]/div/span/div[1]/div/div/div[2]').click()
sleep(5)
dr.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[5]/div[2]/div/span/div[1]/div/span/i/svg').click()
sleep(5)
dr.find_element_by_xpath('//*[text="总管理员"]').click()
sleep(5)\


