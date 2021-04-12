"""
用户意见反馈接口
此接口耦合账号密码登录接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin

class TestFeedback(unittest.TestCase):
    url_feedback = "http://47.114.189.49:8000/member/info/feedback"

    def test_info_feedback(self):
        #   获取登陆身份令牌token
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        data = {
            "phone": "17612282244",
            "reason": "意见反馈测试"
        }
        response = requests.post(url=self.url_feedback, json=data, headers=headers)
        json_info = json.loads(response.text)
        message = json_info['message']
        self.assertEqual("提交成功", message, msg="通过message断言，意见反馈接口报错...")