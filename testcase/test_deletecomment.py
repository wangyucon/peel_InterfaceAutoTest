# """
# 删除评论接口
# 此接口耦合增加一条评论接口 自动调用先增后删
# """
# import unittest
# import requests
# import json
# from peel_interface.testcase import test_UmsMemberLogin,test_addcomment
#
# class TestDeleteComment(unittest.TestCase):
#     url_comment_delete = "http://47.114.189.49:8000/comment/"
#
#     def test_comment_delete(self):
#         #   删除自己增加的评论
#         first_id = test_addcomment.TestAddComment().test_comment()
#
#         peel_token = test_UmsMemberLogin.Testlogin().test_login_six()
#         headers = {'authorization': peel_token}
#
#         response = requests.delete(url=self.url_comment_delete + str(first_id),headers=headers)
#         res = json.loads(response.text)
#         self.assertEqual(res["code"],200)