"""
    登陆模块测试用例
"""

import unittest
import requests

#   账号密码登陆
class Testlogin(unittest.TestCase):
    """
    url：    用户账号密码登陆
    """
    url = "http://47.114.189.49:8000/sso/login/password"
    #   已注册账号 + 六位数字密码 > 登陆
    def test_login_six(self):
        self.data = {
            "authCode": "string",
            "password": "E10ADC3949BA59ABBE56E057F20F883E",
            "phone": "17612282244",
            "platform": "Test",
            "qqUnionid": "string",
            "wbUnionid": "string",
            "wxUnionid": "string"
        }
        response = requests.post(url=self.url,json=self.data)
        self.assertIn("3371220102",response.text)
        return response.headers['authorization']

    #   已注册账号 + 五位数字密码登陆 > 登陆
    def test_login_five(self):
        self.data = {
            "authCode": "string",
            "password": "827CCB0EEA8A706C4C34A16891F84E7B",
            "phone": "17612282244",
            "platform": "Test",
            "qqUnionid": "string",
            "wbUnionid": "string",
            "wxUnionid": "string"
        }
        response = requests.post(url=self.url,json=self.data)
        self.assertIn("账号或密码错误",response.text)

    #   已注册账号 + null密码 > 登陆
    def test_login_null(self):
        self.data = {
            "authCode": "string",
            "password": "",
            "phone": "17612282244",
            "platform": "Test",
            "qqUnionid": "string",
            "wbUnionid": "string",
            "wxUnionid": "string"
        }
        response = requests.post(url=self.url,json=self.data)
        self.assertIn("账号或密码错误", response.text)

    #   非法手机号登陆
    def test_login_phone(self):
        self.data = {
            "authCode": "string",
            "password": "E10ADC3949BA59ABBE56E057F20F883E",
            "phone": "1761228224",
            "platform": "Test",
            "qqUnionid": "string",
            "wbUnionid": "string",
            "wxUnionid": "string"
        }
        response = requests.post(url=self.url,json=self.data)
        self.assertIn("账号或密码错误", response.text)

    #   未注册账号登陆
    def test_login_unregistered(self):
        self.data = {
            "authCode": "string",
            "password": "E10ADC3949BA59ABBE56E057F20F883E",
            "phone": "17612282248",
            "platform": "Test",
            "qqUnionid": "string",
            "wbUnionid": "string",
            "wxUnionid": "string"
        }
        response = requests.post(url=self.url,json=self.data)
        self.assertIn("账号或密码错误", response.text)