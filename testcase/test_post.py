"""
    首页获取帖子列表
    token.yaml、test_data.xlsx临时修改路径（run_all相对路径）
"""
import json
import unittest
import requests
from peel_interface.common.read_excel import *
import os
import yaml
from ruamel.yaml import YAML


class TestPost(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("TestPost模块用例")
        cls.data_list = excel_to_list("./data/test_data.xlsx", "PmsPostController")
        # 获取token.yaml中的身份令牌token
        cls.current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(cls.current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)



    # 未登录状态下获取首页帖子列表
    def test_home_post_list(self):

        case_data = get_test_data(self.data_list, 'test_home_post_list')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    # 登录状态下获取首页帖子列表
    def test_personal_home_post_list(self):
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_personal_home_post_list')
        if not case_data:
            print("用例数据不存在")

        url = case_data.get('url')
        # 期望数据
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url, headers=headers)
        # 断言
        self.assertIn(expect_res, response.text)



    # 获取个人帖子列表
    def test_personal_post_list(self):

        case_data = get_test_data(self.data_list, 'test_personal_post_list')
        if not case_data:
            print("用例数据不存在")

        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url)
        # 断言
        self.assertIn(expect_res, response.text)


    # 获取他人帖子列表
    def test_other_post_list(self):

        case_data = get_test_data(self.data_list, 'test_other_post_list')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        response = requests.get(url=url)
        self.assertIn(expect_res, response.text)


    # 发布商品
    def test_post(self):
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_post')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        # requests.body
        data = case_data.get('data')
        expect_res = case_data.get('expect_res')

        response = requests.post(url=url,headers=headers,json=json.loads(data))
        res = json.loads(response.text)
        self.assertIn(expect_res, response.text)

        # 创建YAML对象
        yaml = YAML()
        # 保存文件路径
        yamlpath = r'.\data\postId.yaml'
        # 提取postId字段
        postIdValue = {
            'postId': res['data']['id']
        }
        # 把postIdValue写入yaml配置文件中
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(postIdValue, f)


    # 获取帖子详情
    def test_post_details(self):


        case_data = get_test_data(self.data_list, 'test_post_details')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')
        # 获取postId.yaml中的postId值
        with open(self.current_path + '\\data' + '\\postId.yaml', 'r') as f:
            self.temp = yaml.load(f.read(), Loader=yaml.FullLoader)

        response = requests.get(url=(url)+str(self.temp['postId']))
        self.assertIn(expect_res, response.text)


    # 删除商品
    def test_post_remove(self):
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_post_remove')
        if not case_data:
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')

        with open(self.current_path + '\\data' + '\\postId.yaml', 'r') as f:
            self.temp = yaml.load(f.read(), Loader=yaml.FullLoader)

        response = requests.delete(url=(url)+str(self.temp['postId']),headers=headers)
        self.assertIn(expect_res, response.text)


