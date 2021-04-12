"""
获取用户个人信息接口
此接口耦合账号密码登录接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin

class TestMemberInfo(unittest.TestCase):
    url_info = "http://47.114.189.49:8000/member/info"

    def test_info(self):
        #   获取登陆身份令牌token
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        response = requests.get(url=self.url_info, headers=headers)
        #   将响应内容转换为Json对象
        json_info = json.loads(response.text)
        #   提取memberId进行断言
        memberid = json_info["data"]['umeMemberBaseInfoDTO']['memberId']
        self.assertEqual(3371219198, memberid, msg="通过member_id断言，获取个人信息接口报错...")