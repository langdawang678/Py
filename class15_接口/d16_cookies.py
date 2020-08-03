
import requests
# 浏览器/postman上，登录后充值，会自动带上cookies
# code上，登录后，再充值。需要把cookies带进去，才能充值成功。
# code带cookies充值成功，可在fiddler中请求headers中看到jsession

login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone": "18111111111", "pwd": "123456"}
res = requests.get(login_url, data)  # 接口文档中定义了get和post都可以
print(res.json())

# 获取cookies
cookies = res.cookies

# 充值(接口定义的入参形式是表单，不是json)
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {"mobilephone": "18111111111", "amount": "1000"}
res = requests.post(url=recharge_url, data=recharge_data, cookies=cookies)
print(res.json())
# {"status":1,"code":"10001","data":{"id":6230,"regname":"柠檬班","pwd":"E10ADC3949BA59ABBE56E057F20F883E","mobilephone":"18111111111","leaveamount":"2648095.00","type":"1","regtime":"2019-05-28 14:14:56.0"},"msg":"充值成功"}

# Session对象去访问，见d16_session.py
# session = requests.Session() # 类似于用code去开启一个浏览器