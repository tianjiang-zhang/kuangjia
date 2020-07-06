from lib2to3.pgen2 import driver

from selenium import webdriver
import unittest,time
from time import sleep
from web_test.data.pian_data import fenlei
from web_test.data.pian_data import plan_data
from web_test.public.Denglu import Deng_lu
from web_test.public.Screen_shot import Screenshot
class Plan_ccase(unittest.TestCase):
    u"""方案"""
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.drive_url ="http://t.yqboom.com"
        dr= self.driver
        dr.get(self.drive_url)

    #@unittest.skip('临时跳过test_caeate_fanan')
    @Screenshot(driver)
    def test_caeate_fanan(self):
        u"""创建方案"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]').click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(2)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('先定1一个小目标')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('王1健林')
        sleep(2)
        dr.find_element_by_xpath(plan_data['地域词库'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['河北省下拉框'][0]).click()
        dr.find_element_by_xpath(plan_data['石家庄市'][0]).click()
        dr.find_element_by_xpath(plan_data['长安区'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['地域词确认'][0]).click()
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).send_keys('先挣他一个亿')
        sleep(2)
        dr.find_element_by_id(plan_data['排除词'][0]).send_keys('无敌')
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        wcao = dr.find_element_by_xpath('/html/body/div[16]/h2').text
        self.assertEqual(wcao,'成功',msg='错误，数据正常但是创建失败')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()

    #@unittest.skip('临时跳过test_fanan_ceiling')
    def test_caeate_fanan_ceiling(self):
        u"""已达方案上限，查看能否创建方案"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        shangxian = dr.find_element_by_xpath(plan_data['方案已达上限'][0]) .text
        self.assertIn(shangxian,"抱歉，方案个数已达上限",msg="错误，已达上限后任能创建方案")
        sleep(2)
        dr.find_element_by_xpath(plan_data['上限弹窗确认'][0]).click()

    #@unittest.skip('临时跳过test_fanan_repeat')
    def test_caeate_fanan_repeat(self):
        u"""使用重复方案名称，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('王健林')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('王健林')
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).send_keys('先定一个小目标')
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        repeat = dr.find_element_by_xpath(plan_data['方案名重复'][0]).text
        self.assertIn(repeat,'方案名重复', msg='错误，方案名称重复也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()

    #@unittest.skip('临时跳过test_fanan_empty')
    def test_caeate_fanan_empty(self):
        u"""方案名称为空，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('王健林')
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).send_keys('先定一个小目标')
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        rmpty = dr.find_element_by_xpath(plan_data['请输入方案名称'][0]).text
        self.assertIn(rmpty,'请输入方案名称', msg='错误，方案名称为空也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()

    #@unittest.skip('临时跳过test_fanan_empty2')
    def test_caeate_fanan_empty2(self):
        u"""主体词为空，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('王健林')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('')
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).send_keys('先定一个小目标')
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        rmpty2 = dr.find_element_by_xpath(plan_data['请输入主体词'][0]).text
        self.assertIn(rmpty2,'请输入主体词', msg='错误，主体词为空也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()


    #@unittest.skip('临时跳过test_fanan_Thephrase_ceiling')
    def test_caeate_fanan_Thephrase_ceiling(self):
        u"""词组超出五组，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('王健林1')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('啧啧啧 我去 威威 侵权 威威 嗯嗯')
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).send_keys('先定一个小目标')
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        cizu = dr.find_element_by_xpath(plan_data['方案内的词组数不得超过5个'][0]).text
        self.assertIn(cizu,'方案内的词组数不得超过5个', msg='错误，词组超出五组也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()

    #@unittest.skip('临时跳过test_fanan_Thephrase_ceiling2')    #  等下一期
    def test_caeate_fanan_Thephrase_ceiling2(self):
        u"""词组为空，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('王健林1')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('啧啧啧 我去 威威 侵权 嗯嗯')
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['删除词组1'[0]]).click()
        dr.find_element_by_xpath(plan_data['删除词组2'[0]]).click()
        dr.find_element_by_xpath(plan_data['删除词组3'[0]]).click()
        dr.find_element_by_xpath(plan_data['删除词组4'[0]]).click()
        dr.find_element_by_xpath(plan_data['删除词组5'[0]]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        cizu2 = dr.find_element_by_xpath(plan_data['方案内的词组数不得超过5个'][0]).text
        self.assertIn(cizu2,'方案内的词组数不得超过5个', msg='错误，词组超出五组也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()

    @unittest.skip('临时跳过test_fanan_name')
    def test_caeate_fanan_name(self):
        u"""方案名称超出20个汉字，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('王健林1啧啧啧 我去 威威 侵权 威威 嗯嗯啧啧啧 我去 威威 侵权 威威 嗯嗯啧啧啧 我去 威威 侵权 威威 嗯嗯')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('啧啧啧 我去 威威 侵权 威威 嗯嗯')
        sleep(2)
        dr.find_element_by_id(plan_data['事件词'][0]).send_keys('先定一个小目标')
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        fanan_name = dr.find_element_by_xpath(plan_data['方案名称不得超过20个汉字'][0]).text
        self.assertIn(fanan_name,'方案名称不得超过20个汉字', msg='错误，方案名称超出20个汉字也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()

    @unittest.skip('临时跳过test_fanan_territory')
    def test_caeate_fanan_territory(self):
        u"""地域词超出100个汉字，查看能否创建方案"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['添加方案'][0]).click()
        sleep(5)
        dr.find_element_by_id(plan_data['方案名称'][0]).send_keys('王健林1啧啧啧 ')
        sleep(2)
        dr.find_element_by_id(plan_data['主体词'][0]).send_keys('啧啧啧 我去 ')
        sleep(2)
        dr.find_element_by_xpath(plan_data['地域词库'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['河北省复选框'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['河北省下拉框'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['唐山市复选框'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['石家庄市下拉框'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['长安区复选框'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['地域词确认'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(4)
        territory = dr.find_element_by_xpath(plan_data['地域词不能超过100个汉字'][0]).text
        self.assertIn(territory,'地域词不能超过100个汉字', msg='错误，方案名称超出20个汉字也能创建成功')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()


    @unittest.skip('临时跳过test_The_editor1')
    def test_The_editor1(self):
        u"""编辑方案——方案分类后查看当前分类方案数是否刷新"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['编辑方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['方案分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['分类二'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        sleep(2)
        wcao = dr.find_element_by_xpath('/html/body/div[16]/h2').text
        self.assertEqual(wcao,'成功',msg='创建失败')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()
        sleep(3)
        fananshu =dr.find_element_by_xpath(plan_data['方案分类数'][0]).text
        self.assertIn(fananshu,'0',msg='错误，方案数没有刷新')


    @unittest.skip('临时跳过test_The_editor')
    def test_The_editor(self):
        u"""编辑方案——方案分类"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['编辑方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['方案分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['分类二'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['保存'][0]).click()
        wcao = dr.find_element_by_xpath('/html/body/div[16]/h2').text
        self.assertEqual(wcao,'成功',msg='创建失败')
        sleep(4)
        dr.find_element_by_xpath(plan_data['创建完成—确认'][0]).click()
    @unittest.skip('临时跳过test_delete_plan')
    def test_delete_plan(self):
        u"""删除方案_删除方案后查看当前分类方案数是否刷新"""
        dr = self.driver
        sleep(20)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['查看方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['删除方案'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(plan_data['确认删除方案'][0]).click()











    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()





















