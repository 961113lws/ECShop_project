# @Time : 2020/10/10 16:19
# @Author : Administrator
# @Email : 2636419668@qq.com
# @File : base_page.py
# @Project : ECShop
"""添加页面基类"""
class BasePage():
    def __init__(self,driver):
        self.driver = driver
