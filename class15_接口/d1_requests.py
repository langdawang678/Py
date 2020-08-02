import requests
"""
get的demo
"""
url = "http://www.baidu.com"
res = requests.get(url)
print(res)  # <Response [200]>
print(type(res))  # <class 'requests.models.Response'>
print(res.text)  #
print(type(res.text))  # <class 'str'>


headers = {"token": "123"}
url = "http://localhost:5000/login"

# 通过params传递query_string参数，Python里就是个字典（如下data）
data = {"username": "aaaa", "pwd": "123456"}

# request.get(url, params=None, **kwargs)
res = requests.get(url, params=data, headers=headers)
# 这里的 params= 和headers= 可以省略，因为是位置参数，写上了就是关键字参数。
print(res.json())  # <class 'dict'>