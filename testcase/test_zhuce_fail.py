# @Time : 2020/10/12 11:00
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : test_zhuce_fail.py
# @Project : ECShop
"""注册成功的用例"""
import unittest
from page.fail_page import FailPage
from page.zhuce_page import ZhucePage
from testcase.base_case import BaseCase
from time import sleep


class TestZhuce(BaseCase):
    def test_zhuce_fail01(self):
        """Ecshop_ST_HYGL_009"""
        """测试注册失败"""
        # 准备测试数据
        username = "ws"
        email = "264575588@qq.com"
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
        sleep(3)
        # #断言注册失败
        dy = FailPage(self.driver)
        yemian = dy.get_fail()
        self.assertEqual(yemian, "系统信息")


    def test_zhuce_fail02(self):
        """Ecshop_ST_HYGL_010"""
        """测试注册失败"""
        # 准备测试数据
        username = "zshr"
        email = "@qq.com"
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
        sleep(3)
        # #断言注册失败
        dy = FailPage(self.driver)
        yemian = dy.get_fail01()
        self.assertEqual(yemian, "* 邮件地址不合法")


if __name__ == '__main__':
    unittest.main()