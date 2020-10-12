# @Time : 2020/10/10 16:19
# @Author : Administrator
# @Email : 2636419668@qq.com
# @File : home_page.py
# @Project : ECShop
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class HomePage(BasePage):
    zhuce_user_locator = (By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(2)")

    # 获取已注册用户元素的内容
    def get_user(self):
        element = self.driver.find_element(*self.zhuce_user_locator)
        text = element.text
        return text