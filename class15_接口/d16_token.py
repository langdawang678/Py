import requests

# 登录接口
# token放在什么地方？
url = "http://120.78.128.25:8766/futureloan/member/login"

headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}
res = requests.post(url, json=data, headers=headers)
print(type(res))  # <class 'requests.models.Response'>
print(type(res.json()))  # <class 'dict'>
print(res.json())

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

# 充值
# token在上一个登录成功后获得，headers要哪些在接口文档中定义
recharge_url = "http://120.78.128.25:8766/futureloan/member/recharge"
token = res.json()["data"]["token_info"]["token"]
id = res.json()["data"]["id"]
headers = {"X-Lemonban-Media-Type": "lemonban.v2",
           "Authorization": f"Bearer {token}"}
data = {
    "member_id": id,
    "amount": 100
}
res = requests.post(recharge_url, json=data, headers=headers)
print(res.json())