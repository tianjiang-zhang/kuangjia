# coding:utf-8
# from selenium import webdriver

class Screenshot(object):
    """这个应该截图功能的装饰器"""

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                now_Time = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file("D:\\kuangjia\\screenshots\\%s.png" % now_Time)
                raise
        return inner