import unittest
import requests
from peel_interface.common.read_excel import *
import os
import yaml


class TestCommentController(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data_list = excel_to_list("../data/test_data.xlsx", "CommentController")
        #   获取登陆身份令牌token
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)
            print(cls.temp['token'])


    def test_comment_null(self):

        case_data = get_test_data(self.data_list, 'test_comment_null')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    def test_comment(self):

        case_data = get_test_data(self.data_list, 'test_comment')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    def test_sencond_comment(self):

        case_data = get_test_data(self.data_list, 'test_sencond_comment')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)

    # def test_insert_comment(self):
    #
    # def test_insert_sencond_comment(self):

    def test_delete_comment(self):

        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_delete_comment')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.delete(url=url, headers=headers)
        self.assertIn(expect_res, response.text)