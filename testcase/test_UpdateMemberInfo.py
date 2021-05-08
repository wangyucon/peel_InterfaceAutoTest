"""
修改用户个人信息接口
此接口耦合账号密码登录接口
"""
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
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        with open(current_path + '\\data' + '\\token.yaml', 'r') as f:
            cls.temp = yaml.load(f.read(), Loader=yaml.FullLoader)
            print(cls.temp['token'])

    def test_info_get(self):
        #   获取登陆身份令牌token
        # peel_token = Testlogin().test_login_success()
        headers = {'authorization': self.temp['token']}

        case_data = get_test_data(self.data_list, 'test_info_get')
        if not case_data:   # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')  # 期望数据

        response = requests.get(url=url,headers=headers)
        self.assertIn(expect_res,response.text)
        print(response.text)



