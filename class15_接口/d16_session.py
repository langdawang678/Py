"""
顺着d16_cookies.py的cookies基础上，用session对象去调用接口
"""
import requests
# Session对象去访问，见d16_cookies_session.py
session = requests.Session()  # 类似于用code去开启一个浏览器

login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone": "18111111111", "pwd": "123456"}
res = session.post(login_url, data)  # 改为request改为session；方法改为post
'''
res = session.get(login_url, data)，提示“TypeError: get() takes 2 positional arguments but 3 were given”
因为session模块中的session类中：def get(self, url, **kwargs):
而requests模块中是直接定义方法：def get(url, params=None, **kwargs):
所以改成如下也可以成功： res = session.get(login_url, params=data)
'''
print(res.json())

# 充值(接口定义的入参形式是表单，不是json)
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {"mobilephone": "18111111111", "amount": "1000"}
res = session.post(url=recharge_url, data=recharge_data)  # 不需要cookies
print(res.json())

session.close()  # 一般不关没事，多个session的可能会混乱
