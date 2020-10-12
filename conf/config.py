# @Time : 2020/10/10 16:17
# @Author : Administrator
# @Email : 2636419668@qq.com
# @File : config.py
# @Project : ECShop
import os
"""封装url"""
zhuce_url = "http://192.168.1.164/upload/user.php?act=register"
Base_path = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
Case_path = os.path.join(Base_path,'testcase')
Report_path = os.path.join(Base_path,'report')