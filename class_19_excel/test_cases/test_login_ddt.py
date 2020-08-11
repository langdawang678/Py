import unittest

import ddt
import warnings

from class_19_excel.common.excel_handler import ExcelHandler
from class_19_excel.common.requests_handler import RequestsHandler

test_data = [
    {"url": "http://120.78.128.25:8766/futureloan/member/login",
     "method": "post",
     "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
     "data": {"mobile_phone": "18111111111", "pwd": "12345678"},
     "expected": "hello world"
     },
    {"url": "http://120.78.128.25:8766/futureloan/member/login",
     "method": "post",
     "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
     "data": {"mobile_phone": "1811", "pwd": "123"},
     "expected": "hello world"
     }
]

@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        # 去掉ResourceWarning: Enable tracemalloc to get the object allocation traceback

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    @ddt.data(*test_data)
    # 将 *test_data中的一组数据，赋值到data_info这个参数
    def test_login_success(self, data_info):
        # def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        '''
        # 实际的入参要根据接口来，d16_token.py中有，
        headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
        data = {"mobile_phone": "18111111111", "pwd": "12345678"}
        res = requests.post(url, json=data, headers=headers)
        '''
        # res = RequestsHandler.visit(data["url"],TypeError: visit() missing 1 required positional argument: 'method'
        res = RequestsHandler().visit(data_info["url"],
                                      data_info["method"],
                                      json=data_info["data"],
                                      headers=data_info["headers"])
        print(type(res))  # <class 'dict'>, 因为visit函数中已经 return res.json()
        '''
        {
        'code': 0, 
        'msg': 'OK', 
        'data': 
            {
            'id': 2049538, 'leave_amount': 502124.01, 'mobile_phone': '18111111111', 'reg_name': '小柠檬', 'reg_time': '2020-07-21 22:57:32.0', 'type': 1, 
            'token_info': 
                {
                'token_type': 'Bearer', 'expires_in': '2020-08-09 21:33:52', 
                'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwNDk1MzgsImV4cCI6MTU5Njk4MDAzMn0.APdL9WJcyk1zL8g1F6G4vQ5KiNoYpOSk-9m4zz7kmco-vpyL0Dw3j_hIF6WX43yfYArY7qZSki847X6qxGXWqw'
                }
            }, 
        'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'
        }
        '''
        # self.assertEqual(res, data["expected"])
        self.assertEqual(res["msg"], "OK")

    # def test_login_error(self):
    #     data = test_data[1]
    #     res = RequestsHandler.visit(data["url"],
    #                                 data["method"],
    #                                 json=data["data"],
    #                                 headers=data["headers"])

if __name__ == '__main__':
    unittest.main()
