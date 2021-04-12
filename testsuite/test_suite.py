"""
测试用例集合运行
"""
import unittest
from peel_interface.testcase.test_personalpost import TestPersonalPost
from peel_interface.testcase.test_addcomment import TestAddComment
from peel_interface.testcase.test_firstcomment import TestFirstComment
from peel_interface.testcase.test_secondcomment import TestSecondComment
from peel_interface.testcase.test_deletecomment import TestDeleteComment
from peel_interface.testcase.test_postlike import TestPostLike
from peel_interface.testcase.test_commentlike import TestCommentLike
from peel_interface.testcase.test_post import TestPost
from peel_interface.testcase.test_feedback import TestFeedback
from peel_interface.testcase.test_logout import TestLogout
from peel_interface.testcase.test_memberinfo import TestMemberInfo
from peel_interface.testcase.test_UpdateMemberInfo import TestUpdateInfo
from peel_interface.testcase.test_withdraw import TestWithdraw
from HTMLTestReportCN import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTests([TestMemberInfo("test_info"),                        #   获取个人信息接口
                TestUpdateInfo("test_info_nickname"),               #   修改个人信息——昵称接口
                TestFeedback("test_info_feedback"),                 #   意见反馈接口
                TestWithdraw("test_info_withdraw"),                 #   注销申请接口
                TestPost("test_post_get"),                          #   首页获取帖子列表接口
                TestDeleteComment("test_comment_delete"),           #   删除帖子接口  自动先调用新增帖子接口
                TestPostLike("test_post_like"),                     #   帖子点赞接口  自动先调用获取个人帖子列表接口
                TestCommentLike("test_comment_like"),               #   一级评论点赞接口    自动先调用获取一级评论列表接口
                TestCommentLike("test_comment_like_second")         #   二级评论点赞接口    自动先调用获取二级评论列表接口
                ])
# unittest.TextTestRunner(verbosity=2).run(suite)
f = open("../testreport/report.html", 'wb') # 二进制写格式打开要生成的报告文件
HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)
f.close()


