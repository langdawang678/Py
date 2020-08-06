import requests

"""
封装requests方法
"""


class HttpHandler:
    def __init__(self):
        self.session = requests.Session()

    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        """
        根据入参method判断请求的方法
        """
        # if method.lower() == "get":
        #     res = self.session.get(url, params=params, **kwargs)
        # elif method.lower == "post":
        #     res = self.session.post(url, params=params, data=data, json=json, **kwargs)
        # else:

        # sessions模块里的Session()类的request方法，可以自动判断method
        '''
            def request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        '''
        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("result is not json ")


httpHandle = HttpHandler()
httpHandle.visit("https://wwww.baidu.com", "get", )  # result is not json
