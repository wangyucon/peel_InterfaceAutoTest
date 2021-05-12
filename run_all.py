import unittest
from peel_interface.testsuite.HTMLTestReportCN import HTMLTestRunner


suite = unittest.defaultTestLoader.discover("./")

with open("./testreport/report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
