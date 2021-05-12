"""
个人信息模块测试用例
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
        print('TestUpdateInfo模块用例')
        cls.data_list = excel_to_list("./data/test_data.xlsx", "UpdataMemberInfo")
        #   获取登陆身份令牌token
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)

    # 获取个人信息
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

    # 修改个人信息——头像
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


    # 修改个人信息——背景图
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


    # 修改个人信息——昵称
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


    # 修改个人信息——性别
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


    # 修改个人信息——简介
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

