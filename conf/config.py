# @Time : 2020/10/10 16:17
# @Author : Administrator
# @Email : 2636419668@qq.com
# @File : config.py
# @Project : ECShop
import os
"""封装注册url"""
zhuce_url = "http://192.168.1.164/upload/user.php?act=register"
"""封装删除注册用户url"""
base_path = os.path.dirname(os.path.abspath(__file__)).split('conf')[0]
case_path = os.path.join(base_path,'testcase')
report_path = os.path.join(base_path,'report')