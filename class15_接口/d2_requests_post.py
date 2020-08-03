"""
post的demo,入参的在fiddler的校验
# requests.post(url, data=None, json=None, **kwargs)
# 也就是可变参数有params，headers，cookies
"""

import requests

headers = {"dalao": "y", "sing_dog": "yuz"}
url = "http://localhost:5000/login"

# 参数传递方式1：query string，在url中
params = {"username": "flybird", "admin": "bawa"}

# 参数传递方式2：form-data（表单），在请求体中
form_data = {"form_admin": "benben"}

# 参数传递方式3：json，在请求体中（json和表单只能存在一种，对应的是一种content-type）
json_data = {"json_data": "shenhai"}

# requests.post(url, data=None, json=None, **kwargs)
# 也就是可变参数有params，headers，cookies
res = requests.post(url, data=form_data, json=json_data, headers=headers, params=params)
# data和json都传入时，只接受data，即webforms的
