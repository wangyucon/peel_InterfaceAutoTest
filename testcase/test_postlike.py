"""
增加帖子点赞记录接口  传入postId
此接口耦合登录接口、获取个人帖子列表接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_UmsMemberLogin,test_personalpost

class TestPostLike(unittest.TestCase):
    url_post_like = "http://47.114.189.49:8000/like?postId=8457325026"

    def test_post_like(self):
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        response = requests.post(url=self.url_post_like,headers=headers)
        res = json.loads(response.text)
        #   提取帖子喜欢状态
        post_likeStatus = test_personalpost.TestPersonalPost().test_post_personal()

        #   通过接口返回信息以及点赞状态判断该帖子是否点赞成功
        if res["message"] == "该帖子你已经赞过了～":  #
            print("该帖子已被你赞过")
        elif post_likeStatus is not "null":
            print("点赞作品成功~")
        else:
            print("点赞作品失败~!")



