"""
评论点赞接口
此接口耦合获取一级评论接口、获取二级评论接口、账号密码登陆接口
"""
import unittest
import requests
import json
from peel_interface.testcase import test_firstcomment,test_secondcomment,test_UmsMemberLogin

class TestCommentLike(unittest.TestCase):
    url_comment_like = "http://47.114.189.49:8000/like/commentId?commentId="
    #   一级评论点赞
    def test_comment_like(self):

        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        response = requests.post(url=self.url_comment_like + str(16239), headers=headers)
        res = json.loads(response.text)
        #   提取帖子一级评论喜欢状态
        comment = test_firstcomment.TestFirstComment()
        comment_likeStatus = comment.test_getComment()["likeStatus"]

        #   通过接口返回信息以及点赞状态判断该评论是否点赞成功
        if res["message"] == "该评论你已经赞过了～":
            print("该评论你已经赞过了～")
        elif comment_likeStatus is not "null":
            print("点赞评论成功~")
        else:
            print("点赞评论失败~!")

        #   二级评论点赞
    def test_comment_like_second(self):
        peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
        headers = {'authorization': peel_token}

        response = requests.post(url=self.url_comment_like + str(17416), headers=headers)
        res = json.loads(response.text)
        #   提取帖子二级评论喜欢状态
        comment2 = test_secondcomment.TestSecondComment()
        comment_likeStatus_second = comment2.test_getComment_second()["likeStatus"]

        #   通过接口返回信息以及点赞状态判断该评论是否点赞成功
        if res["message"] == "该评论你已经赞过了～":
            print("该评论你已经赞过了～")
        elif comment_likeStatus_second is not "null":
            print("点赞评论成功~")
        else:
            print("点赞评论失败~!")