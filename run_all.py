import unittest

from testsuite.HTMLTestReportCN import HTMLTestRunner


suite = unittest.defaultTestLoader.discover("./testcase")

with open("./testreport/report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)
