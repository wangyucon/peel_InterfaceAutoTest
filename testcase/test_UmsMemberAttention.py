import unittest

import requests
from common.read_excel import *
import os
import yaml


class TestMemberAttention(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('TestMemberAttention模块用例')
        cls.data_list = excel_to_list("./data/test_data.xlsx", "UmsAttentionController")
        #   获取登陆身份令牌token
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)


    # 别人空关注列表
    def test_attention_list_null(self):

        case_data = get_test_data(self.data_list, 'test_attention_list_null')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    # 别人空粉丝列表
    def test_fans_list_null(self):

        case_data = get_test_data(self.data_list, 'test_fans_list_null')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    # 关注
    def test_other_attention(self):

        headers = {'authorization': self.temp['token']}
        case_data = get_test_data(self.data_list, 'test_attention')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.post(url=url,headers=headers)
        self.assertIn(expect_res, response.text)


    # 获取关注列表
    def test_other_attention_list(self):

        case_data = get_test_data(self.data_list, 'test_other_attention_list')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    # 获取粉丝列表
    def test_other_fans_list(self):

        case_data = get_test_data(self.data_list, 'test_other_fans_list')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    # 互相关注
    def test_other_mutual_attention(self):

        headers = {'authorization': self.temp['token']}
        case_data = get_test_data(self.data_list, 'test_other_mutual_attention')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.post(url=url,headers=headers)
        self.assertIn(expect_res, response.text)


    # 获取个人关注列表
    def test_personal_attention_list(self):

        headers = {'authorization': self.temp['token']}
        case_data = get_test_data(self.data_list, 'test_personal_attention_list')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url,headers=headers)
        self.assertIn(expect_res, response.text)


    # 获取个人粉丝列表
    def test_personal_fans_list(self):

        headers = {'authorization': self.temp['token']}
        case_data = get_test_data(self.data_list, 'test_personal_fans_list')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url,headers=headers)
        self.assertIn(expect_res, response.text)

    # 取消关注
    def test_remove_attention(self):

        headers = {'authorization': self.temp['token']}
        case_data = get_test_data(self.data_list, 'test_remove_attention')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.delete(url=url,headers=headers)
        self.assertIn(expect_res, response.text)


    # 取消关注
    def test_remove_attention1(self):

        headers = {'authorization': self.temp['token']}
        case_data = get_test_data(self.data_list, 'test_remove_attention1')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.delete(url=url,headers=headers)
        self.assertIn(expect_res, response.text)