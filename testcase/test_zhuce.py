# @Time : 2020/10/11 22:10
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : test_zhuce.py
# @Project : ECShop
"""注册成功的用例"""
import unittest
from page.home_page import HomePage
from page.zhuce_page import ZhucePage
from testcase.base_case import BaseCase
import random
from time import sleep
class TestZhuce(BaseCase):

    def test_zhuce01(self):
        """Ecshop_ST_HYGL_001"""
        """username输入为三位，其他输入合法"""
        # 准备测试数据
        # username = "DTHD"
        username = random.sample("qwertyuiopasdfghjklzxcvbnm", 3)
        emai = random.randint(100,100000000000000)
        emai1=str(emai)
        email=emai1+"@qq.com"
        password = "123456"
        confirm_password = password
        print(username)

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # 断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce02(self):
        """Ecshop_ST_HYGL_002"""
        """username输入15位，其他输入合法"""
        # 准备测试数据
        username = "abcdefghijklmn"
        email = "26440053333@qq.com"
        password = "123456"
        confirm_password = "123456"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # 断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce03(self):
        """Ecshop_ST_HYGL_003"""
        """username输入7位，其他输入合法"""
        # 准备测试数据
        username = "abcdefg"
        email = "33440053333@qq.com"
        password = "123456"
        confirm_password = "123456"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # #断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce04(self):
        """Ecshop_ST_HYGL_004"""
        """email输入前缀三位，其他输入合法"""
        # 准备测试数据
        username = "abcde"
        email = "264@qq.com"
        password = "123456"
        confirm_password = "123456"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # #断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce05(self):
        """Ecshop_ST_HYGL_005"""
        """email前缀输入15位，其他输入合法"""
        # 准备测试数据
        username = "abcdefghij"
        email = "264400533330001@qq.com"
        password = "123456"
        confirm_password = "123456"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # #断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce06(self):
        """Ecshop_ST_HYGL_006"""
        """email前缀输入10位，其他输入合法"""
        # 准备测试数据
        username = "abc"
        email = "2644005666@qq.com"
        password = "1234567891"
        confirm_password = "1234567891"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # #断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce07(self):
        """Ecshop_ST_HYGL_007"""
        """password和confirm—password输入25位，其他输入合法"""
        # 准备测试数据
        username = "ling"
        email = "26440058883@qq.com"
        password = "1234567891234567891234567"
        confirm_password = "1234567891234567891234567"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # #断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")


    def test_zhuce08(self):
        """Ecshop_ST_HYGL_008"""
        """password和confirm—password输入15位，其他输入合法"""
        # 准备测试数据
        username = "shu"
        email = "26448858683@qq.com"
        password = "12345678912345"
        confirm_password = "12345678912345"

        # 用例步骤
        # 实例化注册页面对象
        lp = ZhucePage(self.driver)
        # 打开注册页面
        lp.open_page()
        # 输入用户名
        lp.input_username(username)
        # 输入邮箱
        lp.input_email(email)
        # 输入密码
        lp.input_password(password)
        # 输入确认密码
        lp.input_confirm_password(confirm_password)
        # 点击注册
        lp.click_submit()
        # #断言注册成功
        dy = HomePage(self.driver)
        yemian = dy.get_user()
        self.assertEqual(yemian,"退出")

if __name__ == '__main__':
    unittest.main()