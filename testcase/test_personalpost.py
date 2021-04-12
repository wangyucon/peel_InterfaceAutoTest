"""
获取个人帖子列表接口
此接口耦合帖子点赞接口
"""
import unittest
import requests
import json
class TestPersonalPost(unittest.TestCase):
    url_post_personal = "http://47.114.189.49:8000/post/personal?memberId=3371219200&pageNum=1&pageSize=5"

    def test_post_personal(self):
        response = requests.get(url=self.url_post_personal)
        self.assertIn("好看的裙子万里挑一", response.text)
        res = json.loads(response.text)
        return res['data'][0]['likeStatus'] #   返回该帖子喜欢状态