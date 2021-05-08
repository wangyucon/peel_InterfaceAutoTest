"""
    登陆模块测试用例
"""
import json
import unittest
import requests
from ruamel import yaml

from peel_interface.common.read_excel import *



class Testlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('已调用login函数')
        cls.data_list = excel_to_list("../data/test_data.xlsx", "UmsMemberLogin")


    # 输入已注册的用户名和正确的密码，验证是否成功登录
    def test_login_success(self):

        case_data = get_test_data(self.data_list, 'test_login_success')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url, json=json.loads(data))
        self.assertIn(expect_res, response.text)
        # return response.headers['authorization']
        # 把token值写入配置文件中
        yamlpath = r'D:\test_software\pythonProject\peel_interface\data\token.yaml'  # 保存文件路径
        # 提取token字段
        tokenValue = {
            'token': response.headers['authorization']
        }
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(tokenValue, f, Dumper=yaml.RoundTripDumper)




    # 输入已注册的用户名和不正确的密码，验证是否成功失败
    def test_login_pwd_error(self):

        case_data = get_test_data(self.data_list, 'test_login_pwd_error')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url,json=json.loads(data))
        self.assertEqual(expect_res, response.text)


    #   输入未注册的用户名和任意密码，验证是否登录失败
    def test_login_phone_error(self):

        case_data = get_test_data(self.data_list, 'test_login_phone_error')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url,json=json.loads(data))
        self.assertEqual(expect_res, response.text)


    #   用户名和密码两者都为空，验证是否登录失败
    def test_login_null(self):

        case_data = get_test_data(self.data_list, 'test_login_null')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url, json=json.loads(data))
        self.assertEqual(expect_res, response.text)


    #   密码为空，验证是否登录失败
    def test_login_pwd_null(self):

        case_data = get_test_data(self.data_list, 'test_login_pwd_null')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url, json=json.loads(data))
        self.assertEqual(expect_res.strip(), response.text)


    # 用户名为空，验证是否登录失败
    def test_login_phone_bull(self):

        case_data = get_test_data(self.data_list, 'test_login_phone_bull')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url, json=json.loads(data))
        self.assertEqual(expect_res.strip(), response.text)
