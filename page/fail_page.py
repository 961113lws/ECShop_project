# @Time : 2020/10/12 10:56
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : fail_page.py
# @Project : ECShop
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class FailPage(BasePage):
    """注册失败信息定位器"""
    zhuce_fail_locator = (By.XPATH,"/html/body/div[6]/div/div/div/div/p[1]")   # /html/body/div[6]/div/div/div/div/p[1]
    zhuce_fail01_locator = (By.XPATH,"//*[@id='email_notice']")
    # 获取已注册用户元素的内容
    def assert_zhuce_fail(self):
        element = self.driver.find_element(*self.zhuce_fail_locator)
        text = element.text
        return text

    def tishi_message(self):
        element = self.driver.find_element(*self.zhuce_fail01_locator)
        text = element.text
        return text