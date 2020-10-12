# @Time : 2020/10/11 21:01
# @Author : Administrator
# @Email : 2636419668@qq.com
# @File : zhuce_page.py
# @Project : ECShop

"""封装注册页面"""
from selenium.webdriver.common.by import By
from conf.config import zhuce_url
from page.base_page import BasePage
import random

class ZhucePage(BasePage):
    # 封装定位器
    # 用户名输入定位器
    username_locator = (By.NAME,"username")
    # 邮箱输入定位器
    email_locator = (By.NAME,"email")
    # 密码输入定位器
    password_locator = (By.NAME,"password")
    # 确认密码输入定位器
    confirm_password_locator = (By.NAME,"confirm_password")
    # 点击会员注册定位器
    submit_locator = (By.NAME,"Submit")

    # 输入用户名
    def input_username(self,username):
        """找到用户名并输入用户名"""
        element = self.driver.find_element(*self.username_locator)
        element.clear()
        element.send_keys(username)

    # 输入邮箱
    def input_email(self,email):
        element = self.driver.find_element(*self.email_locator)
        element.clear()
        element.send_keys(email)

    # 输入密码
    def input_password(self,password):
        element = self.driver.find_element(*self.password_locator)
        element.clear()
        element.send_keys(password)

    # 输入确认密码
    def input_confirm_password(self,confirm_password):
        element = self.driver.find_element(*self.confirm_password_locator)
        element.clear()
        element.send_keys(confirm_password)

    # 点击会员注册
    def click_submit(self):
        element = self.driver.find_element(*self.submit_locator)
        element.click()

    # 进入页面
    def open_page(self):
        self.driver.get(zhuce_url)