# """
# 增加一条评论接口
# 此接口耦合登录接口
# """
# import unittest
# import requests
# import json
# from peel_interface.testcase import test_UmsMemberLogin
#
# class TestAddComment(unittest.TestCase):
#     url_comment = "http://47.114.189.49:8000/comment"
#     def test_comment(self):
#         peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
#         headers = {'authorization': peel_token}
#         data = {
#             "content": "增加一条一级评论",
#             "postId": 8457325026
#         }
#         response = requests.post(url=self.url_comment ,headers=headers ,json=data)
#         res = json.loads(response.text)
#         self.assertEqual(res["code"] ,200)
#         return res['data']