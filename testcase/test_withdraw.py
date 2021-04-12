"""
退出登录接口
此接口耦合账号密码登录接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin

class TestWithdraw(unittest.TestCase):
    url_withdraw = "http://47.114.189.49:8000/member/info/withdraw"

    #   退出登录接口
    def test_info_withdraw(self):
        #   获取登陆身份令牌token
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        response = requests.post(url=self.url_withdraw, headers=headers)
        json_info = json.loads(response.text)
        code = json_info['code']
        self.assertEqual(200, code)