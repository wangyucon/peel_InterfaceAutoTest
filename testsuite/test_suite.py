import unittest
from peel_interface.testcase.test_UmsMemberLogin import Testlogin
from peel_interface.testcase.test_UpdateMemberInfo import TestUpdateInfo

suite = unittest.TestSuite()
suite.addTest(Testlogin('test_login_success')) # 添加单个用例
suite.addTest(TestUpdateInfo('test_info_get')) # 添加多个用例

# 运行测试集
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序


