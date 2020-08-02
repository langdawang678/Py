from flask import Flask
"""
建立一个本地服务器，用于requests的get和post验证
"""
app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    return {"msg": "success!"}  # 响应头Content-Type值是application/json
    # return "success", 200  # 响应头Content-Type值是text/html; charset=utf-8
# /login地址和login()函数绑定在一起，访问地址的时候，函数被调用
if __name__ == '__main__':
    app.run()
