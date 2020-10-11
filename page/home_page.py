# @Time : 2020/10/10 16:19
# @Author : Administrator
# @Email : scg@gmail.com
# @File : home_page.py
# @Project : ECShop
from selenium.webdriver.common.by import By
from page.base_page import Basepage

class HomePage(Basepage):
    zhuce_user_locator = (By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(1)")

    # 获取已注册用户元素的内容
    def get_user(self):
        element = self.driver.find_element(*self.zhuce_user_locator)
        text = element.text
        return  text