# @Time : 2020/10/12 10:37
# @Author : 帅帅
# @Email : 2636419668@qq.com
# @File : runner.py
# @Project : ECShop
import unittest
import time
from conf.config import case_path,report_path
from BeautifulReport import BeautifulReport

"""执行所有用例"""

# 创建测试集
suite = unittest.defaultTestLoader.discover(case_path,"test_*.py")
# 创建执行器
runner = BeautifulReport(suite)
# 执行
filename = "{}{}.html".format("ECShop-report-",time.strftime("%Y%m%d%H%M"))
runner.report(description="ECShop测试报告",
              filename=filename,
              report_dir=report_path)