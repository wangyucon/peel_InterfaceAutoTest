"""
增加/删除帖子点赞记录接口
"""
import unittest
import requests
from peel_interface.common.read_excel import *
import os
import yaml


class TestPostLike(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('TestPostLike模块用例')
        cls.data_list = excel_to_list("./data/test_data.xlsx", "PmsPostLikeController")
        #   获取登陆身份令牌token
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)


    # 增加帖子点赞记录
    def test_post_like(self):
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_post_like')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url, headers=headers)
        self.assertIn(expect_res, response.text)


    # 点赞已点赞过的帖子
    def test_post_like_fail(self):
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_post_like_fail')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.post(url=url, headers=headers)
        self.assertIn(expect_res, response.text)


    # 删除帖子点赞记录
    def test_post_like_off(self):
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_post_like_off')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.delete(url=url, headers=headers)
        self.assertIn(expect_res, response.text)



