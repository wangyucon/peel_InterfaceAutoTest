"""
获取二级评论列表
此接口耦合账号密码登录接口、评论点赞接口（一二级）
"""
import unittest
import requests
import json

class TestSecondComment(unittest.TestCase):
    url_getComment_second = "http://47.114.189.49:8000/comment/second/16017?pageNum=1&pageSize=10"

    def test_getComment_second(self):
        response = requests.get(url=self.url_getComment_second)
        res = json.loads(response.text)
        self.assertEqual(res["code"], 200)
        return res["data"][1]   #   返回第二条二级评论内容