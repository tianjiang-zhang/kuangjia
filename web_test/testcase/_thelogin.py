from selenium import webdriver
import unittest,time
from time import sleep
from web_test.data.The_login_data import the_Login

class The_login(unittest.TestCase):
    u"""登录"""
    driver = webdriver.Firefox()
    @classmethod
    def setUp(self):
        dr = self.driver
        dr.get("http://t.yqboom.com")

    def test_denglu(self):
        u"""查看能否正常登录"""
        dr = self.driver
        dr.find_element_by_xpath(the_Login['登录试用'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号登录'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号名'][0]).send_keys('test1')
        sleep(1)
        dr.find_element_by_xpath(the_Login['密码'][0]).send_keys('123456')
        sleep(1)
        dr.find_element_by_xpath(the_Login['提交'][0]).click()
        sleep(5)
        title = dr.title
        self.assertEqual(title,'无极大数据',msg='title不是无极大数据')
        sleep(5)
        text1 = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]').text
        sleep(3)
        self.assertEqual(text1, 'test1', msg='没有登录成功')
        if u'无极大数据' == dr.title:
            print('用例通过，登录成功')
        else:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"错误,账号密码输入正确但不能正常登录")



    def test_wer_2(self):
        u"""账号错误查看能否正常登录"""
        sleep(5)
        dr = self.driver
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


    def test_qwe_3(self):
        u"""密码错误查看能否正常登录"""
        sleep(5)
        dr = self.driver
        dr.find_element_by_xpath(the_Login['登录试用'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号登录'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号名'][0]).send_keys('test1')
        sleep(1)
        dr.find_element_by_xpath(the_Login['密码'][0]).send_keys('1234567')
        sleep(1)
        dr.find_element_by_xpath(the_Login['提交'][0]).click()
        sleep(5)
        qwe =dr.find_element_by_xpath('/html/body/div/div/div[1]/p/img').is_displayed()
        self.assertTrue(qwe, msg='错误,密码输入错误可以正常登录')
        try:
            self.assertTrue(qwe,)
            print('用例3通过')
        except AssertionError as e:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"错误,账号输入错误可以正常登录")
        sleep(5)


    def test_denglu_4(self):
        u"""账号密码错误查看能否正常登录"""
        dr = self.driver
        dr.find_element_by_xpath(the_Login['登录试用'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号登录'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(the_Login['账号名'][0]).send_keys('test11')
        sleep(1)
        dr.find_element_by_xpath(the_Login['密码'][0]).send_keys('1234567')
        sleep(1)
        dr.find_element_by_xpath(the_Login['提交'][0]).click()
        sleep(5)
        rty = dr.find_element_by_xpath('/html/body/div/div/div[1]/p/img').is_displayed()
        self.assertTrue(rty, msg='错误,账号密码输入错误可以正常登录')
        try:
            self.assertTrue(rty,)
            print('用例4通过')
        except AssertionError as e:
            current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            pic_path = ("D:\\kuangjia\\screenshots\\" + current_time + ".png")
            print(pic_path)
            self.driver.save_screenshot(pic_path)
            print(u"错误,账号输入错误可以正常登录")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()





























