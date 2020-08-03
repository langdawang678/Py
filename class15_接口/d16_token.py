import requests

# 登录接口
# token放在什么地方？
url = "http://120.78.128.25:8766/futureloan/member/login"

headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
data = {"mobile_phone": "18111111111", "pwd": "12345678"}
res = requests.post(url, json=data, headers=headers)
print(res.json())

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