"""
获取一级评论接口
此接口耦合账号密码登录接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin

class TestFirstComment(unittest.TestCase):
    
    url_getComment = "http://47.114.189.49:8000/comment/8457325026?pageNum=1&pageSize=10"

    peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
    headers = {'authorization': peel_token}

    def test_getComment(self):
        response = requests.get(url=self.url_getComment)
        res = json.loads(response.text)
        self.assertEqual(res["code"],200)
        return res["data"]["dto"][0]   #   返回第一条一级评论内容


