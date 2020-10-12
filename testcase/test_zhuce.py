# @Time : 2020/10/11 22:10
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : test_zhuce.py
# @Project : ECShop
"""注册成功的用例"""
import unittest
from page.home_page import HomePage
from page.zhuce_page import Zhucepage
from testcase.base_case import Basecase
import random
class Testzhuce(Basecase):
    def test_zhuce(self):
        """测试注册成功"""
        # 准备测试数据
        username = "ling"
        email = "2646419668@qq.com"
        password = "123456"
        confirm_password = "123456"

        #用例步骤
        #实例化注册页面对象
        lp = Zhucepage(self.driver)
        #打开注册页面
        lp.open_page()
        #输入用户名
        lp.input_username(username)
        #输入邮箱
        lp.input_email(email)
        #输入密码
        lp.input_password(password)
        #输入确认密码
        lp.input_confirm_password(confirm_password)
        #点击注册
        lp.click_submit()
        # #断言注册成功
        # dy = HomePage(self.driver)
        # yemian = dy.get_user()
        # self.assertEqual()

if __name__ == '__main__':
    unittest.main()