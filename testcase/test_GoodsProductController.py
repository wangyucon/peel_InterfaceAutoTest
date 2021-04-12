"""
二手商品相关接口
"""
import json
# from peel_interface.testcase.excel_data import ExcelData
import ddt
import requests
import unittest

@ddt.ddt
class TestGoods(unittest.TestCase):

    #   会员账号密码登陆
    @ddt.file_data('D:\\test_software\pythonProject\peel_interface\common\login.json')
    @ddt.unpack
    def test_login_six(self,value):
        print(value[0])
        data = {
            "authCode": "string",
            "password": value[0]['user'],
            "phone": value[0]['password'],
            "platform": "Test",
            "qqUnionid": "string",
            "wbUnionid": "string",
            "wxUnionid": "string"
        }
        response = requests.post(url='http://116.62.204.155:8000/sso/login/password',json=data)
        print(response.text)
        self.assertIn("3371219195",response.text)
        return response.headers['authorization']

    #   获取一级类目
#     def test_category1(self):
#         response = requests.get('http://116.62.204.155:8000/product/goodsCategory')
#         paren_id = json.loads(response.text)['data'][0]['parentId']
#         print(response.text)
#         self.assertEqual(paren_id,0)
#
#     #   获取子级类目
#     def test_category2(self):
#         peel_token = TestGoods.test_login_six(self)
#         headers = {'authorization': peel_token}
#         response = requests.get('http://116.62.204.155:8000/product/goodsCategory/2',headers = headers)
#         print(response.text)
#
#     #   集市首页获取商品列表
#     def test_goods_list(self):
#         response = requests.get('http://116.62.204.155:8000/product/list?pageNum=1&pageSize=10')
#         print(response.text)
#
#     #   获取二手商品详情
#     def test_goods_infomation(self):
#         response = requests.get('http://116.62.204.155:8000/product/1')
#
#     #   获取品牌
#     def test_getbrand(self):
#         response = requests.get('http://116.62.204.155:8000/product/brand?pageNum=1&pageSize=20')
#         print(response.text)
#
#     #   搜索品牌
#     def test_search_brand(self):
#         peel_token = TestGoods.test_login_six(self)
#         headers = {'authorization': peel_token}
#         response = requests.get('http://116.62.204.155:8000/product/brandSearch/jk',headers=headers)
#         print(response.text)
#
#     #   通过属性值parentId获取子属性
#     def test_parentid(self):
#         peel_token = TestGoods.test_login_six(self)
#         headers = {'authorization': peel_token}
#         response = requests.get('http://116.62.204.155:8000/product/attributeValue/parentId/1', headers=headers)
#         print(response.text)
#
#     #   通过类目获取对应的属性名和属性值
#     def test_categoryid(self):
#         peel_token = TestGoods.test_login_six(self)
#         headers = {'authorization': peel_token}
#         response = requests.get('http://116.62.204.155:8000/product/attribute?categoryId=15', headers=headers)
#         print(response.text)
#
#     #   发布二手商品
#     def test_publish(self):
#         peel_token = TestGoods.test_login_six(self)
#         headers = {'authorization': peel_token}
#         data = {
#             "brandId": 2,
#             "brandName": "中牌制服馆",
#             "categoryId": 15,
#             "categoryName": "关东襟",
#             "commonIndexes": "string",
#             "createTime": "2021-04-01T02:43:26.891Z",
#             "description": "正品保证，专柜小票支持验货",
#             "getMoney": 75,
#             "goodsTitle": "温柔一刀",
#             "keyIndexes": "['款式':'昭和']",
#             "picture": "https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/3338950428/O1CN01cz2PeR1F246arRPuA_!!0-item_pic.jpg_580x580Q90.jpg_.webp,https://g-search3.alicdn.com/img/bao/uploaded/i4/i3/3373660421/O1CN01H3Gx2r1EyrLL3JMiI_!!3373660421.jpg_580x580Q90.jpg_.webp,https://g-search1.alicdn.com/img/bao/uploaded/i4/i2/1789669770/O1CN01cCabkY2M2iBX8TJv9_!!1789669770-0-lubanu-s.jpg_580x580Q90.jpg_.webp",
#             "price": 100,
#             "saleIndexes": "['纽扣样式':'一粒纽']",
#             "secondHandIndexes": "[状态:穿一洗一]",
#             "serviceMoney": 5,
#             "shippingMoney": 20
# }
#         response = requests.post(url='http://116.62.204.155:8000/product',json=data,headers=headers)
#         print(response.text)

    #   数据驱动测试


# suite = unittest.TestSuite()
# suite.addTest(TestGoods('test_login_six_1'))
# runner = unittest.TextTestRunner()
# runner.run(suite)

if __name__ == '__main__':
    unittest.main()
