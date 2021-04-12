"""
修改用户个人信息接口
此接口耦合账号密码登录接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin

class TestUpdateInfo(unittest.TestCase):
    url_info = "http://47.114.189.49:8000/member/info"

    def test_info_nickname(self):
        #   获取登陆身份令牌token
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}
        data = {
        "nickname": "昵称修改"
        }
        response = requests.put(url=self.url_info,headers=headers,json=data)
        json_info = json.loads(response.text)
        message = json_info['message']
        self.assertEqual("编辑成功",message,msg="通过message断言，修改个人信息接口报错...")



