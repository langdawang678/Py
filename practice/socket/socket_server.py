"""
服务器端套接字，bind，listen，accept
"""
import socket

server = socket.socket()    # 创建 socket 对象
server.bind(("127.0.0.1", 8080))    # 绑定ip和端口；这里是元组，所以有两个括号
server.listen(5)    # 设置最大连接数，超过后排队
while True:
    sock, addr = server.accept()    # 被动接受TCP客户端连接,(阻塞式)等待连接的到来;点开源码发现这里返回了两个
    print("连接地址是：", addr)
    sock.send(b"welcome")   # bytes类型
    sock.send("welcome2".encode("utf-8"))  # bytes类型
    sock.close()

'''
字符串的前缀
一、b前缀表示：后面字符串是bytes 类型。
网络编程中，服务器和浏览器只认bytes 类型数据。
在 Python3 中，bytes 和 str 的互相转换方式是
str.encode('utf-8')
bytes.decode('utf-8')
'''
'''
二、
前缀r，表示去掉反斜杠的转义，长用于正则或者路径地址
三、
前缀u，表示以 Unicode 格式 进行编码，一般用在中文字符串前面
'''