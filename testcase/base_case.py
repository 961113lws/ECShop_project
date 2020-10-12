# @Time : 2020/10/10 16:20
# @Author : Administrator
# @Email : 2636419668@qq.com
# @File : base_case.py
# @Project : ECShop

import unittest
from model.driver import browser_chrome
class BaseCase(unittest.TestCase):
    """所有测试用例基类"""
    def setUp(self) -> None:
        self.driver = browser_chrome()

    def tearDown(self) -> None:
        self.driver.quit()