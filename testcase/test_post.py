"""
    首页获取帖子列表
"""
import unittest
import requests

class TestPost(unittest.TestCase):
    url_post = "http://47.114.189.49:8000/post?pageNum=1&pageSize=300"

    def test_post_get(self):
        response = requests.get(url=self.url_post)
        self.assertIn("jk",response.text)
