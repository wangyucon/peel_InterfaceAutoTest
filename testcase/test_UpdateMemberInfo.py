"""
修改用户个人信息接口
此接口耦合账号密码登录接口
"""
import json
import unittest
import requests
from peel_interface.common.read_excel import *
import os
import yaml

class TestUpdateInfo(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        print('以调用info函数')
        cls.data_list = excel_to_list("../data/test_data.xlsx", "UpdataMemberInfo")
        #   获取登陆身份令牌token
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)
            print(cls.temp['token'])


    def test_info_get(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_get')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.get(url=url,headers=headers)
        self.assertIn(expect_res,response.text)
        print(response.text)


    def test_info_edit_avatar(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_edit_avatar')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.put(url=url,headers=headers,json=json.loads(data))
        self.assertEqual(expect_res,response.text)


    def test_info_edit_backgroundImage(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_edit_backgroundImage')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.put(url=url,headers=headers,json=json.loads(data))
        self.assertEqual(expect_res,response.text)


    def test_info_edit_nickname(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_edit_nickname')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.put(url=url,headers=headers,json=json.loads(data))
        self.assertEqual(expect_res,response.text)


    def test_info_edit_sex(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_edit_sex')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.put(url=url,headers=headers,json=json.loads(data))
        self.assertEqual(expect_res,response.text)


    def test_info_edit_signature(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_edit_signature')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.put(url=url,headers=headers,json=json.loads(data))
        self.assertEqual(expect_res,response.text)

