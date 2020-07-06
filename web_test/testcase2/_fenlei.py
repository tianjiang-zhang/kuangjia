from selenium import webdriver
import unittest,time
from time import sleep
import verify
from assertpy import assert_that
from data.pian_data import fenlei
from collections.abc import Iterable
import ssl
from public.Denglu import Deng_lu
from selenium.webdriver.common.keys import Keys


class Fenlei_case(unittest.TestCase):
    u"""分类"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.drive_url ="http://t.yqboom.com"
        dr= self.driver
        dr.get(self.drive_url)
    #@unittest.skip('临时跳过test_create_fenlei_Chinese') #跳过这条测试用例
    def test_create_fenlei_Chinese(self):
        u"""创建分类——使用汉字创建"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(10)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('我的天啊啊啊')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()
        sleep(2)
        ss= dr.find_element_by_xpath(fenlei['文本定位断言'][0]).is_displayed()# 断言定位到的信息是否可见
        dr.assertTextPresent(ss)  # 检查在当前给用户显示的页面上是否有出现指定的文本
        sleep(2)

    #@unittest.skip('临时跳过test_create_fenlei_digital')
    def test_create_fenlei_digital(self):
        u"""创建分类——使用数字创建"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('1270214')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(10)
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()
        sleep(5)
        shuzi = dr.find_element_by_xpath('/html/body/div[21]/p').text
        self.assertIn(shuzi,"分类创建成功",msg="使用数字创建分类失败")

    #@unittest.skip('临时跳过test_create_fenlei_English')
    def test_create_fenlei_English(self):
        u"""创建分类——使用英文创建"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('wai')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(5)
        yinwen = dr.find_element_by_xpath('/html/body/div[21]/p').text
        self.assertIn(yinwen, "分类创建成功", msg="使用英文创建分类失败")
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    @unittest.skip('临时跳过test_create_fenlei_character')
    def test_create_fenlei_character(self):
        u"""创建分类——使用特殊字符创建"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('！@#￥%')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(5)
        teshu = dr.find_element_by_xpath('/html/body/div[21]/p').text
        self.assertIn(teshu, "分类创建成功", msg="使用特殊符号创建分类失败")
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    #@unittest.skip('临时跳过test_create_fenlei_ceiling')
    def test_create_fenlei_ceiling(self):
        u"""创建分类——超出边界值能否创建"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('一二三四五六七八九十啊')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(2)
        cuowu = dr.find_element_by_xpath('/html/body/div[21]/h2').text
        sleep(5)
        self.assertEqual(cuowu,'错误',msg='错误，超出上限也能创建成功')
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    @unittest.skip('临时跳过test_create_fenlei_Equa')
    def test_create_fenlei_Equal(self):
        u"""创建分类——使用已存在的名称能否创建"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('wain')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(5)
        chofu = dr.find_element_by_xpath('/html/body/div[21]/h2').text
        self.assertEqual(chofu,'错误', msg='错误，使用重复名称也能创建成功')
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    #@unittest.skip('临时跳过test_create_fenlei_interrupt')
    def test_create_fenlei_interrupt(self):
        u"""创建时点击其他模块再切换回来完成创建，查看能创建成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('啧啧啧')
        sleep(2)
        dr.find_element_by_xpath(fenlei['数据大屏'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        zhoduan =  dr.find_element_by_xpath('/html/body/div[21]/p').text
        sleep(2)
        self.assertIn(zhoduan,"分类创建成功", msg="创建时中断，再创建分类失败")
        sleep(2)
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    #@unittest.skip('临时跳过test_create_fenlei_empty')
    def test_create_fenlei_empty(self):
        u"""创建分类——分类名称使用空格能否创建，"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys(' ')
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(5)
        kog = dr.find_element_by_xpath('/html/body/div[21]/h2').text
        self.assertEqual(kog,'错误', msg='错误，使用空格名称也能创建成功')
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    #@unittest.skip('临时跳过test_create_fenlei_empty2')
    def test_create_fenlei_empty2(self):
        u"""创建分类——分类名称为空查看能否创建，"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击新建分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        sleep(5)
        ko = dr.find_element_by_xpath('/html/body/div[21]/p').text
        self.assertEqual(ko,'请输入方案名称', msg='错误，分类名称为空也能创建成功')
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()





    @unittest.skip('临时跳过test_create_fenlei_interrupt')
    def test__editor_fenlei_increase(self):
        u"""编辑分类时，分类名称增加一位字符查看能编辑成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('嗯')
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys(Keys.BACKSPACE)
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑确认'][0]).click()
        sleep(5)
        zenjia = dr.find_element_by_xpath(fenlei['分类编辑成功'][0]).text
        self.assertIn(zenjia,'分类编辑成功',msg="增加一位汉字后编辑失败")
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    @unittest.skip('临时跳过test_create_fenlei_detele')
    def test__editor_fenlei_detele(self):
        u"""编辑分类时，分类名称删除一位字符查看能编辑成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys(Keys.BACKSPACE)
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑确认'][0]).click()
        sleep(5)
        shanchu = dr.find_element_by_xpath(fenlei['分类编辑成功'][0]).text
        self.assertIn(shanchu,'分类编辑成功',msg="删除一位汉字后编辑失败")
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    @unittest.skip('临时跳过test_create_fenlei_repeat')
    def test__editor_fenlei_repeat(self):
        u"""编辑分类时，将分类名称修改为已存在的名称查看能否编辑成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['清除文本框文本信息'][0]).clear()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('啧啧啧')
        dr.find_element_by_xpath(fenlei['点击编辑确认'][0]).click()
        sleep(5)
        chofu = dr.find_element_by_xpath(fenlei['分类名称不能重复'][0]).text
        self.assertIn(chofu,'分类名称不能重复',msg="将分类名称修复为已存在的名称后编辑成功")
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    @unittest.skip('临时跳过test_create_fenlei_beyond')
    def test__editor_fenlei_beyond(self):
        u"""编辑分类时，将分类名称修改为十一位字符名称查看能否编辑成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('啧吱吱吱吱在啧啧')
        dr.find_element_by_xpath(fenlei['点击编辑确认'][0]).click()
        sleep(5)
        chaochu = dr.find_element_by_xpath(fenlei['方案名称不得超过十个汉字'][0]).text
        self.assertIn(chaochu,'方案名称不得超过十个汉字',msg="将分类名称修改十一位字符名称后编辑成功")
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()

    @unittest.skip('临时跳过test_editor_fenlei_interrupt')
    def test_editor_fenlei_interrupt(self):
        u"""编辑时点击其他模块再切换回来完成创建，查看能创建成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击编辑分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['输入分类名称'][0]).send_keys('啧啧啧')
        sleep(2)
        dr.find_element_by_xpath(fenlei['数据大屏'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        zhoduan2 =  dr.find_element_by_xpath('/html/body/div[16]/p').text
        sleep(2)
        self.assertIn(zhoduan2,"分类编辑成功",msg="编辑时中断，再创建分类失败")
        sleep(2)
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()


    @unittest.skip('临时跳过test_detele_fenlei_shanchu')
    def test_detele_fenlei_shanchu(self):
        u"""删除没有方案的分类，查看能否删除成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['删除分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['确认删除'][0]).click()
        sleep(2)
        sc = dr.find_element_by_xpath('/html/body/div[16]/p').text
        self.assertIn(sc,'分类删除成功',msg='删除不成功')

    @unittest.skip('临时跳过test_detele_fenlei_There')
    def test_detele_fenlei_There(self):
        u"""删除有方案的分类，查看是否给出提示信息"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['删除分类'][0]).click()
        sleep(5)
        dr.find_element_by_xpath('/html/body/div[8]/div[1]/div[6]/div/p[2]').is_displayed()
        dr.find_element_by_xpath(fenlei['确认删除'][0]).click()

    @unittest.skip('临时跳过test_detele_fenlei_zhoduansc')
    def test_detele_fenlei_zhoduansc(self):
        u"""删除时点击其他模块再切换回来完成删除，查看能删除成功"""
        deng_lu = Deng_lu(self.driver)
        deng_lu.denglu()
        dr = self.driver
        sleep(5)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击删除分类'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['数据大屏'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击个人中心'][0]).click()
        sleep(2)
        dr.find_element_by_xpath(fenlei['点击确认'][0]).click()
        schu =  dr.find_element_by_xpath(fenlei['分类删除成功'][0]).text
        sleep(2)
        self.assertIn(schu,"分类删除成功",msg="删除时中断，再删除失败")
        sleep(2)
        dr.find_element_by_xpath(fenlei['弹窗确认'][0]).click()


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()