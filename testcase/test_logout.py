"""
注销申请接口
此接口耦合账号密码登录接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin

class TestLogout(unittest.TestCase):
    url_logout = "http://47.114.189.49:8000/member/info/logout"

    #   注销申请
    def test_info_logout(self):
        #   获取登陆身份令牌token
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        data = {
            "phone": "17612282244",
            "reason": "意见反馈测试"
        }
        response = requests.post(url=self.url_logout, json=data, headers=headers)
        json_info = json.loads(response.text)
        message = json_info['message']
        self.assertEqual("您已提交过注销申请。", message, msg="通过message断言，注销申请接口报错...")
