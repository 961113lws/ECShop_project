# @Time : 2020/10/10 16:18
# @Author : Administrator
# @Email : 2636419668@.com
# @File : driver.py
# @Project : ECShop
from selenium import webdriver

def browser_chrome():
    """封装谷歌浏览器"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
